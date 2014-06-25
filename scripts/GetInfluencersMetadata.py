# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

#get EchoNest metadata on beats influencers playlists

import requests
import json
from json import load
from pprint import pprint 
import urllib2
from urllib2 import urlopen
import pandas as pd
from pandas import *
import numpy as np
import urllib
import csv
from collections import defaultdict
from Beats2EchoNest import beats2echonest

#import a .csv file with all playlists from a particular influencer

data = []
track_list = []
with open('/home/vanessa/NHRInsightFL/influencerstrainingset.csv', 'rb') as csvfile:
    reader = csv.DictReader(csvfile, ['id', 'user_id', 'playlist_id','subscribers','track_id'])
    for row in reader:
        data.append(row)
#use track ids to 
#find song names
for song in data:
    t = song['track_id']
    track_list.append(t)

tattle = track_list[1:200]
EN_id_list = beats2echonest(tattle)
print EN_id_list


#pass a list of the track_ids to beats2echonest to get echonest IDs
#beats2echonest(track_id)

#call 

# <codecell>


# <codecell>


# <codecell>


