# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from flask import render_template, request

import pymysql
import requests
import json
from json import load
from pprint import pprint 
import urllib2
from urllib2 import urlopen
import pandas as pd
from pandas import *
import numpy as np
import time
import codecs
from FindPlaylistPopularity import spopularity


db = pymysql.connect(host="127.0.0.1", user="NickiRom", db = "test")
cursed = db.cursor()
string = ""
myquery = 'pl145609517957120000'
if(cursed.execute("SELECT track_id FROM firsttable WHERE playlist_id=\"" + myquery.encode('utf-8')+"\"")):
    result = cursed.fetchall()
    newtuple = (); 
    for index in result:
        newtuple = (index,);
        #print newtuple
        string = string + str(newtuple[0][0]) + "\n"
        print string
        
    #firstresult= result[0][0]
    print firstresult

# <codecell>


# <codecell>


