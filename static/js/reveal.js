Reveal.initialize({

    // Display controls in the bottom right corner
    controls: true,

    // Display a presentation progress bar
    progress: true,

    // Display the page number of the current slide
    slideNumber: false,

    // Push each slide change to the browser history
    history: false,

    // Enable keyboard shortcuts for navigation
    keyboard: true,

    // Enable the slide overview mode
    overview: true,

    // Vertical centering of slides
    center: true,

    // Enables touch navigation on devices with touch input
    touch: true,

    // Loop the presentation
    loop: false,

    // Change the presentation direction to be RTL
    rtl: false,

    // Turns fragments on and off globally
    fragments: true,

    // Flags if the presentation is running in an embedded mode,
    // i.e. contained within a limited portion of the screen
    embedded: false,

    // Number of milliseconds between automatically proceeding to the
    // next slide, disabled when set to 0, this value can be overwritten
    // by using a data-autoslide attribute on your slides
    autoSlide: 0,

    // Stop auto-sliding after user input
    autoSlideStoppable: true,

    // Enable slide navigation via mouse wheel
    mouseWheel: false,

    // Hides the address bar on mobile devices
    hideAddressBar: true,

    // Opens links in an iframe preview overlay
    previewLinks: false,

    // Transition style
    transition: 'default', // default/cube/page/concave/zoom/linear/fade/none

    // Transition speed
    transitionSpeed: 'default', // default/fast/slow

    // Transition style for full page slide backgrounds
    backgroundTransition: 'default', // default/none/slide/concave/convex/zoom

    // Number of slides away from the current that are visible
    viewDistance: 3,

    // Parallax background image
    parallaxBackgroundImage: '',
    // e.g. "'https://s3.amazonaws.com/hakim-static/reveal-js/reveal-parallax-1.jpg'"

    // Parallax background size
    parallaxBackgroundSize: '2100px 900px',
    // CSS syntax, e.g. "2100px 900px"

    dependencies: [
        // Cross-browser shim that fully implements classList - https://github.com/eligrey/classList.js/
        { src: 'static/vendor/components-revealjs/lib/js/classList.js',
            condition: function() { return !document.body.classList; } },

        // Interpret Markdown in <section> elements
        { src: 'static/vendor/components-revealjs/plugin/markdown/marked.js',
            condition: function() { return !!document.querySelector( '[data-markdown]' ); } },
        { src: 'static/vendor/components-revealjs/plugin/markdown/markdown.js',
            condition: function() { return !!document.querySelector( '[data-markdown]' ); } },

        // Syntax highlight for <code> elements
        { src: 'static/vendor/components-revealjs/plugin/highlight/highlight.js',
            async: true, callback: function() { hljs.initHighlightingOnLoad(); } },

        // Zoom in and out with Alt+click
        { src: 'static/vendor/components-revealjs/plugin/zoom-js/zoom.js',
            async: true, condition: function() { return !!document.body.classList; } },

        // Speaker notes
        { src: 'static/vendor/components-revealjs/plugin/notes/notes.js',
            async: true, condition: function() { return !!document.body.classList; } }
    ]
});
