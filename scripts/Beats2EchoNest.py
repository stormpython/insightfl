# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

# search for EchoNest ids based on track name and duration

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

#takes a list of BeatsMusic track ids and returns a list of the EchoNest track ids
def beats2echonest(track_id):
    beats_url = 'https://partner.api.beatsmusic.com/v1/api/tracks/'

    #initialize list of identifier dicts
    identifier = []
    EN_id_list = []
    
    for tracks in track_id:
        beats_url = 'https://partner.api.beatsmusic.com/v1/api/tracks/'
        #print tracks
        query = tracks + "?"
        client_id = 'client_id=cu4dweftqe5nt2wcpukcvgqu'
        beats_url = beats_url + query + client_id
        #print beats_url
        
        response = requests.get(beats_url)
        json_obj = json.loads(response.text)
     
            
        trackname = json_obj['data']['title'].encode('utf-8')
        artist = json_obj['data']['artist_display_name'].encode('utf-8')
        duration = json_obj['data']['duration']
        min_duration = int(duration)*0.95
        max_duration = int(duration)*1.05
        
        tidentifier = {'artist':artist,'title':trackname, 'max_duration':max_duration, 'min_duration':min_duration}
        tidentifier = urllib.urlencode(tidentifier)
        identifier.append(tidentifier)
    
    #search for track in Echonest
    EN_id = []
    
    for codes in identifier:
        #print tracks
        apikey = 'W89S7QJCCHFARWJGD'
        jsonformat = '&format=json&results=1&'
        summary_request = '&bucket=audio_summary'
        
        url ='http://developer.echonest.com/api/v4/song/search?api_key=' + apikey + jsonformat + codes+  summary_request        
        

        response = urllib2.urlopen(url)

        json_obj = json.load(response)
        if len(json_obj['response']['songs'])==0:
            EN_id = ' '
        else:
            EN_id = json_obj['response']['songs'][0]['id']
        EN_id_list.append(EN_id.encode('utf-8'))
    
    
    return EN_id_list

# <codecell>


# <codecell>


