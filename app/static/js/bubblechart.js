(function (data) {
    'use strict';

    /* Bubble Chart */
    var margin,
        width,
        height,
        x,
        y,
        color,
        xAxis,
        yAxis,
        svg,
        text,
        bubbles;

    // Establishing chart margins, width, and height.
    margin = { top: 20, right: 20, bottom: 50, left: 100 },
    width = 960 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

    // Creating the x scale.
    x = d3.scale.linear().range([0, width]);

    // Creating the y scale.
    y = d3.scale.linear().range([height, 0]);

    // Built in d3 color function.
    color = d3.scale.category20();

    // Function which draws the x axis.
    xAxis = d3.svg.axis().scale(x).orient("bottom");

    // Function which draws the y axis.
    yAxis = d3.svg.axis().scale(y).orient("left");

    // Drawing the canvas.
    svg = d3.select("#chart").append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    data.forEach(function (d) {
        d.country = d.country;
        d.gdp = +d.gdp;
        d.edu_index = +d.edu_index;
        d.median_age = +d.median_age;
    });

    x.domain(d3.extent(data, function (d) { return d.median_age; }));
    y.domain(d3.extent(data, function (d) { return d.edu_index; }));

    // Creating the x axis.
    svg.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + height + ")")
        .call(xAxis)
        .append("text")
        .attr("class", "x label")
        .attr("x", function () { return width/2; })
        .attr("y", 30)
        .attr("dy", ".71em")
        .style("text-anchor", "middle")
        .text("Median Age");

    // Creating the y axis.
    svg.append("g")
        .attr("class", "y axis")
        .call(yAxis)
        .append("text")
        .attr("class", "y label")
        .attr("transform", "rotate(-90)")
        .attr("y", -60)
        .attr("x", -height/2)
        .attr("dy", ".71em")
        .style("text-anchor", "middle")
        .text("Education Index");

    // Creating clipPath
    svg.append("clipPath")
        .attr("id", "chart-area")
        .append("rect")
        .attr("x", 0)
        .attr("y", 0)
        .attr("width", width)
        .attr("height", height);

    // Creating the bubble chart.
    bubbles = svg.append("g")
        .attr("id", "circles")
        .attr("clip-path", "url(#chart-area)")
        .selectAll(".country").append("circle")
        .data(data)
        .enter()
        .append("circle")
        .attr("class", "country")
        .attr("cx", function (d) { return x(d.median_age); })
        .attr("cy", -80)
        .attr("r", function (d) { return Math.log(d.gdp); })
        .style("fill", function (d) { return color(d.country); });

    bubbles
        .transition()
        .duration(2000)
        .delay(function (d, i) { return i * 300; })
        .attr("cx", function (d) { return x(d.median_age); })
        .attr("cy", function (d) { return y(d.edu_index); })
        .attr("r", function (d) { return Math.log(d.gdp); })
        .ease("bounce");

    // Creating the tooltips for the bubble chart.
    bubbles
        .on("mouseover", function (d) {
            var xPosition = parseFloat(d3.select(this).attr("cx"));

            if (d3.select(this).attr("cy") < 140) {
                var yPosition = parseFloat(d3.select(this).attr("cy")) + 50;
            } else {
                var yPosition = parseFloat(d3.select(this).attr("cy")) - 100;
            }

            d3.select("#tooltip")
                .style("left", xPosition + "px")
                .style("top", yPosition + "px")
                .select("#value")
                .html(
                    "Country: " + d.country +
                    "<br>Education Index: " + d.edu_index +
                    "<br>Median Age: " + d.median_age +
                    "<br>GDP: $" + numberWithCommas(d.gdp) + "M"
                );
            d3.select("#tooltip").classed("hidden", false);
        })
        .on("mouseout", function () {
            d3.select("#tooltip").classed("hidden", true);
        });

    // Text for the bubbles. Should include the Country name or abbr.
    // Text should be centered within bubbles.
    text = svg.selectAll(".bubbles").append("text")
        .data(data)
        .enter()
        .append("text")
        .attr("class", "bubbles")
        .attr("x", function (d) { return x(d.median_age); })
        .attr("y", -80)
        .attr("dy", ".71em")
        .style("text-anchor", "middle")
        .text(function (d) { return d.country; });

    text
        .transition()
        .duration(2000)
        .delay(function (d, i) { return i * 300; })
        .attr("x", function (d) { return x(d.median_age); })
        .attr("y", function (d) { return y(d.edu_index); })
        .attr("dy", ".71em")
        .style("text-anchor", "middle")
        .text(function (d) { return d.country; })
        .ease("bounce")
        .remove("text", function (d,i) { return i * 3000; });

    function numberWithCommas(x) {
        return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    }

    return svg;
}( window.data ));