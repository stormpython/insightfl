# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

#given a playlist id from Beats, generate track IDs.  Output of list of track IDs will go to Beats2EchoNest.py.  setlist runs Beats2EchoNest, EN_id2summary, Distance Matrix, Thresholding

import requests
import json
from json import load
from pprint import pprint 
import urllib2
from urllib2 import urlopen
import pandas as pd
from pandas import *
import numpy as np
from numpy import *
import urllib
import scipy
from scipy import *
from scipy.spatial.distance import pdist, wminkowski, squareform
import matplotlib.pyplot as plt
import prettyplotlib as ppl
import networkx as nx
from networkx.algorithms.traversal.depth_first_search import dfs_tree
from collections import defaultdict

def setlist(beats_playlist):
    
    track_id = beatspl2tracks(beats_playlist)
    #print track_id
    
    EN_id_list = beats2echonest(track_id)
    #print EN_id_list
    
    dist_matrix, playlist= EN_id2summary(EN_id_list)
    #print summarydf
    
    
    UTlist = DiGraph(dist_matrix, playlist)
    
    return UTlist
    
    
    
    
    
#--------------------------------------------------------------------
def beatspl2tracks(beats_playlist):
    
    access_token = '?access_token=hr9fk9dftzuzmpnsutqmq95a'
    client_id = '&client_id=cu4dweftqe5nt2wcpukcvgqu'
    
    url = 'https://partner.api.beatsmusic.com/v1/api/playlists/' + beats_playlist + access_token
    response = requests.get(url)
    json_obj = json.loads(response.text)
    pprint(json_obj)
    datum = json_obj['data']['refs']['tracks']
    
    track_id = []
    
    for song in datum:
        t = song['id']
        track_id.append(t.encode('utf-8'))
    
    return track_id

#--------------------------------------------------------------------
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
            continue
            #EN_id = ' '
        else:
            EN_id = json_obj['response']['songs'][0]['id']
        EN_id_list.append(EN_id.encode('utf-8'))
    
    
    return EN_id_list
#--------------------------------------------------------------------


def EN_id2summary(EN_id_list):
    #set up dataframe for collection
    df = pd.DataFrame({'artist': [], 'track_id':[], 'song':[],'key':[], 'tempo':[], 'energy':[], 'liveness':[], 'analysis_url':[], 'speechiness':[], 'acousticness':[], 'danceability':[], 'time_signature':[], 'duration':[], 'loudness':[], 'valence':[], 'mode':[]})

    columns = ['artist','track_id','song','key', 'tempo', 'energy', 'liveness', 'analysis_url', 'speechiness', 'acousticness', 'danceability', 'time_signature', 'duration', 'loudness', 'valence', 'mode']

    for song in EN_id_list:
        if song == " ":
            tempdf = pd.DataFrame([(" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ")], index = [0], columns = columns)
        else:
            apikey = 'W89S7QJCCHFARWJGD'
            jsonformat = '&format=json&results=1&'
            summary_request = '&bucket=audio_summary'
            id_url = 'id=' + str(song)
            
            url ='http://developer.echonest.com/api/v4/song/profile?api_key=' + apikey + jsonformat + id_url+  summary_request        
            response = urllib2.urlopen(url)
            json_obj = json.load(response)
        
            EN_id = json_obj['response']['songs'][0]['id']
        
            tempdict = json_obj['response']['songs'][0]['audio_summary']
            tempdf = pd.DataFrame(tempdict, index = [1])

            tempdf['artist']= json_obj['response']['songs'][0]['artist_id']
            tempdf['track_id']= json_obj['response']['songs'][0]['id']
            tempdf['song']=json_obj['response']['songs'][0]['title']
    
        df = df.append(tempdf, ignore_index = True)
        

    summarydf = pd.DataFrame(df, columns = columns)

    list_of_songdata = []

    #convert to list of rows (list of lists)
    for i in summarydf.index:
        row = summarydf.ix[i]
        
        rowlist = []
        
        if row['tempo'] == " ":
            rowlist = [" "," "," "," "," "," "]
        else:
            rowlist = [row['track_id'], row['tempo'],row['energy'],row['danceability'],row['loudness'],row['valence']]#track_id
            #print rowlist
            
        list_of_songdata.append(rowlist)


    ranges = zip(*list_of_songdata)[1:]
    #print ranges
    minimum = map(min, ranges)
    maximum = map(max, ranges)
    rangemap = [m-n for m,n in zip( maximum, minimum)]
    
    weights = [float(1/r) for r in rangemap]
    
    X = np.array(list_of_songdata)
    
    X1 = X[:, 1:]
    #print X1
    
    distances = pdist(X1, wminkowski, 2, weights)
    dist_matrix= squareform(distances)
    #print dist_matrix
    
    distancelist = []
    for index in range(0, len(dist_matrix)):
        distancelist.append(dist_matrix[index])
    
    return summarydf, dist_matrix


#------------------------------------------------------------------------------

def DiGraph(dist_matrix, playlist):
    

    #convert to dataframe with trackIDs as columns
    columns = ['a','b','c','d','e','f','g','h','i','k','j','l','m','n','o','p','q','r']
    df = pd.DataFrame(dist_matrix, index = columns, columns = playlist)
    
    index = 0
    row = 2
    
    tups = []
    cols = columns
    
    #put distance matrix into list of lists [[track1, track2, weight],...] for depth first search
    for index1, rows in enumerate(df):
    
        for index, cols in enumerate(df):
            mytups = [df.index[index1], df.columns[index], df.ix[index1][index]]
            tups.append(mytups)
    #transform weights to create a higher penalty for higher weights
    for tup in tups:
        tup[2] = math.e**(tup[2])
    
    
    # get an idea of the distribution of transition scores
    scores = []
    
    for item in tups:
        scores.append(item[2])
    
    scores = sorted(scores, reverse=True)
    
    average_score = sum(scores)/float(len(scores))
    
    '''show histogram of 
    plt.hist(p, bins = 20, cumulative=True)
    plt.show()
    '''
    
    #prune edges from graph by removing lists in the edges list
    for worst in scores:
        for tup in tups:
            if tup[2] >= average_score:
                tups.remove(tup)
            if tup[2] == 1:
                tups.remove(tup)
    
    #build a Directed graph
    DG=nx.DiGraph()
    DG.add_weighted_edges_from(tups)
    #print DG.neighbors('a')
    
    #iterate over all starting songs
    Tlist = []
    orderlist = []
    for node in DG:

        T = nx.dfs_tree(DG,node)
        #print nx.dfs_postorder_nodes(T)
        order = list(v for u,v,d in nx.dfs_labeled_edges(DG,source=node)
          if d['dir']=='reverse')
        orderlist.append(order)
    print orderlist[0]
        
    #print(list(nx.dfs_labeled_edges(T,node)))
    Tlist.append(T)
    #print(list(T.edges()))
    #print Tlist
    
    
    UTlist = []
    for trees in Tlist:
        UT=T.to_undirected()
        #print(nx.connected_components(UT))
        UTlist.append(nx.connected_components(UT))

    return UTlist, orderlist
#---------------------------------------------------------------------------------


# <codecell>


# <codecell>


