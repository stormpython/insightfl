# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import requests
import json
from json import load
from pprint import pprint 
import urllib2
from urllib2 import urlopen
import pandas as pd
from pandas import *
from pandas.tools.plotting import scatter_matrix
import numpy as np
import matplotlib.pyplot as plt
from URI2Echonest import echonestdata

Surl = 'http://ws.spotify.com/lookup/1/.json'


URI = '?uri=spotify:album:574xhx2X0G9MkqACxqi4cg'
extras = '&extras=trackdetail'
Surl = Surl + URI + extras

response = requests.get(Surl)
json_obj = json.loads(response.text)


#initialize track_id
track_ids = []

#make a list of track_ids
for tracks in json_obj['album']['tracks']:
    track_ids.append(tracks['href'].encode("utf-8"))

f = echonestdata(track_ids)
f1 = f[['key','tempo','energy', 'liveness', 'speechiness','acousticness', 'danceability','loudness','valence']]
print f1
scatter_matrix(f1, figsize = (12,8), diagonal = 'kde')
plt.show()

# <codecell>

f1.plot(subplots=True, figsize = (6,6))
plt.legend(loc='best')
plt.show()

# <codecell>


