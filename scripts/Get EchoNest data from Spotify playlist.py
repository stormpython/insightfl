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
import pyechonest
from pyechonest import *
config.ECHO_NEST_API_KEY = 'W89S7QJCCHFARWJGD'
import spotify
from spotify import *

#def echonestinfo(playlist_id, idtype):
    #get track ids:
#if (idtype = "Spotify"):


#from libspotify import *
session = spotify.Session()
#album = session.get_album('spotify:album:0XHpO9qTpqJJQwa2zFxAAE')

#track is for uploading tracks and getting info via analyzer
#songs is for searching

t = track.track_from_id('TRTLKZV12E5AC92E11')
print t.artist
songs = [t]
cols = ["artist", "song_id", "duration", "danceability", "energy", "key", "mode", "tempo", "loudness"]
data = {"artist": [], "song_id":[], "duration":[], "danceability": [], "energy":[], "key":[], "mode":[], "tempo":[], "loudness":[]}
df = pd.DataFrame(data, columns = cols) 

for t in songs:
    newrow = {"artist": t.artist.encode('utf-8'), "song_id":t.song_id.encode('utf-8'), "duration":t.duration, "danceability": t.danceability, "energy":t.energy, "key":t.key, "mode":t.mode, "tempo":t.tempo, "loudness":t.loudness}
    temp = pd.DataFrame(newrow, index = [0], columns = cols)
    df = concat([df,temp], ignore_index = True)
    print df


'''rows_list = []
for row in rows:

        dict1 = {}
        ##Blah Blah .... 
        dict1.update(blah..) 
        rows_list.append(dict1)'''

#df = pd.DataFrame(rows_list)   

#s.get_song_hotttness() gives you the hotttness of a song
a = artist.Artist('girl talk')
aid = a.id
print aid
a = artist.Artist(aid, buckets=['hotttnesss'])
print a.hotttnesss


# <codecell>

df = concat([df,temp], ignore_index = True)
print df

# <codecell>


