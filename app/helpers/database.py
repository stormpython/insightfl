import pymysql
import sys
import simplejson as json


# Returns MySQL database connection
def con_db(host, port, user, passwd, db):
    try:
        con = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db)

    except pymysql.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit(1)

    return con


def world_index(con):
    data_array = []

    cur = con.cursor()
    cur.execute(
        """
        SELECT id, country, median_age, gdp, edu_index
        FROM world_index
        WHERE edu_index >= 0.55
        ORDER BY edu_index DESC
        """
    )

    data = cur.fetchall()
    for country in data:
        index = {}

        index["id"] = country[0]
        index["country"] = country[1]
        index["median_age"] = float(json.dumps(country[2]))
        index["gdp"] = country[3]
        index["edu_index"] = float(json.dumps(country[4]))

        data_array.append(index)

    cur.close()
    return data_array
