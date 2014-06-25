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
import time
import codecs
from FindPlaylistPopularity import spopularity

#import tracklists and playlists.  Tracklists are collections of hit songs; playlists are mixes
tracklists = pd.read_csv('/home/vanessa/NHRInsightFL/toptracklists.csv')
playlists = pd.read_csv('/home/vanessa/NHRInsightFL/topplaylists.csv')

#practice getting info from the Beats API
#first, get user ids for top tastemakers:
access_token = '&access_token=sankyec99twpvqu997awsher'
client_id = '&client_id=cu4dweftqe5nt2wcpukcvgqu'

#influencers PopCrush (pop), RapRadar (rap), Revolver (metal), Stevie Nicks (soft rock), Pitchfork (indie):
user_id = ['126510877590553088', '110464913905943040','117729155298230784','139592358051184896','116993337273221888']

#used to find user ids by keyword
#url = 'https://partner.api.beatsmusic.com/v1/api/search?q='+user_id[0] + '&type=user' + client_id
data = {'user_id':[],'playlist_id':[], 'subscribers':[], 'track_id':[]}


df = pd.DataFrame(data, columns = ['user_id','playlist_id','subscribers', 'track_id'])


traininglist = []



#for loop: iterating over influencers
for index in user_id:
    url = 'https://partner.api.beatsmusic.com/v1/api/users/'+index + '/playlists?limit=100' + access_token
    response = requests.get(url)
    #print response
    
    json_obj = json.loads(response.text)
    datum = json_obj['data']
    #pprint(datum)
    
    playlist = []
    
    index1 = index.encode('utf-8')
    #for loop: iterating over influencer's playlists
    for playlist_no in datum:
        

        listid = playlist_no['id']
        subscribers = playlist_no['total_subscribers']

        p = spopularity(listid)

        trainingtemp = {'pl':listid, 'subscribers':subscribers, 'track_popular':p}
        traininglist.append(trainingtemp)
        #print traininglist
        #train = pd.DataFrame(traininglist, columns = ['playlist_id', 'subscribers', 'track_popular'])
        #train

        
        track_name = []
        playlist1 = playlist_no['refs']['tracks']

        
        #for loop: iterating over playlist's tracks

        for tracks in playlist1:
            track_name.append(tracks['display'])
            track_id = tracks['id'].encode('utf-8')
            
            
            #print subscribers
            tempdata = {'user_id':index1,'playlist_id':listid,'subscribers': subscribers,'track_id':track_id}
            #print tempdata
            temp = pd.DataFrame(tempdata, columns = ['user_id','playlist_id','subscribers', 'track_id'], index = [0])
            df = concat([df, temp], ignore_index=True)
            #print df

 
            
addressname = '/home/vanessa/NHRInsightFL/influencerstrainingset.csv'
df.to_csv(addressname, sep=',', cols =['user_id','playlist_id','subscribers', 'track_id'], header = True, index = True)
train = DataFrame.from_records(traininglist)
train.to_csv('/home/vanessa/NHRInsightFL/traininglist.csv', sep = ',')

# <codecell>


for tracks in playlist1:
    print tracks['id']

# <codecell>


# <codecell>


