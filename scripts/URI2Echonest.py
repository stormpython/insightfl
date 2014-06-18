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
#print track_ids

#----------------------get track details from echonest---------------------------------------------------
def echonestdata(track_list):
    apikey = 'W89S7QJCCHFARWJGD'

    reqjson = '&format=json'
    reqsummary = '&bucket=audio_summary'
    
    #set up dataframe for collection
    df = pd.DataFrame({'artist': [], 'track_id':[], 'song':[],'key':[], 'tempo':[], 'energy':[], 'liveness':[], 'analysis_url':[], 'speechiness':[], 'acousticness':[], 'danceability':[], 'time_signature':[], 'duration':[], 'loudness':[], 'valence':[], 'mode':[]})
    
    
    #change track id catalog to Spotify-ww: and search EchoNest for information
    for tracks in track_list:
        if "spotify" in tracks:
            tracks = tracks.replace("spotify", "&id=spotify-WW")
        else: tracks = "&id=" + tracks
        ENurl ='http://developer.echonest.com/api/v4/track/profile?api_key=' + apikey + reqjson + reqsummary + tracks
        response = requests.get(ENurl)
        data = json.loads(response.text)
        #pprint(data)
        tempdict = data['response']['track']['audio_summary']
        tempdf = pd.DataFrame(tempdict, index = [1])
        tempdf['artist']= data['response']['track']['artist']
        tempdf['track_id']= data['response']['track']['song_id']
        tempdf['song']=data['response']['track']['title']
        #print tempdf
        df = df.append(tempdf, ignore_index = True)
    
    return df
    #df.to_pickle('/home/vanessa/NHRInsightFL/GirlTalkFeedAnimals.pkl')
    
    columns = ['artist','track_id','song','key', 'tempo', 'energy', 'liveness', 'analysis_url', 'speechiness', 'acousticness', 'danceability', 'time_signature', 'duration', 'loudness', 'valence', 'mode']
    #filename = data['response']['track']['release'].encode('utf-8')
    #print filename
    #df.to_csv('/home/vanessa/NHRInsightFL/girltalk.csv', sep=',', cols =columns, header = True, index = True)
#--------------------------------------------------------

f = echonestdata(track_ids)
print f



# <codecell>



# <codecell>


# <codecell>


