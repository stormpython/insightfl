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
import numpy as np



# Looks up the popularity of each song in a playlist; prints the average popularity and returns a dataframe of popularities
def spopularity(playlist_id):
    url = 'https://partner.api.beatsmusic.com/v1/api/playlists/'
    details = '/tracks?limit=100&offset=0'
    access_token = '&access_token=sankyec99twpvqu997awsher'
    url = url + playlist_id + details + access_token

    response = requests.get(url)
    #print response
    json_obj = json.loads(response.text)
    
    list = json_obj['data']
    
    popular = []
    
    for songs in list:
        data = songs['popularity']
        #print data
        popular.append(data)
   
    average = sum(popular)/len(popular)
    print "average is ", average, "popular ", popular," divided by number of tracks", len(popular)
    #print "The average popularity is " + str(average)
    populard = pd.DataFrame(popular, columns = ['Popularity'])
    addressname = '/home/vanessa/NHRInsightFL/influencer_playlists' + playlist_id + '.csv'
    #populard.to_csv(addressname, sep=',', cols =['Popularity'], header = True, index = True)  
    return average







# <codecell>

spopularity('pl145291027756875776')

# <codecell>


