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
import urllib
import csv
from collections import defaultdict
from Beats2EchoNest import beats2echonest
from EN_id2summary import EN_id2summary
from scipy.spatial.distance import pdist, wminkowski, squareform
import matplotlib.pyplot as plt
import prettyplotlib as ppl


#read in playlist data
list_of_songdata = []
with open('/home/vanessa/NHRInsightFL/testing123small.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, ['artist','track_id','song','key', 'tempo', 'energy', 'liveness', 'analysis_url', 'speechiness', 'acousticness', 'danceability', 'time_signature', 'duration', 'loudness', 'valence', 'mode'])
    trow = []
    next(reader)
    #print reader
    for row in reader:
        #print row
        trow = []
        #print row[2]
        trow.append(row[2])

        trow.append(float(row[5]))
        trow.append(float(row[6]))
        trow.append(float(row[11]))
        trow.append(float(row[14]))
        trow.append(float(row[15]))
        #print trow
        list_of_songdata.append(trow)
        
#print list_of_songdata

ranges = zip(*list_of_songdata)[1:]
minimum = map(min, ranges)
maximum = map(max, ranges)
rangemap = [m-n for m,n in zip( maximum, minimum)]
#print rangemap
weights = [float(1/r) for r in rangemap]
#print weights

X = np.array(list_of_songdata)
#print X
X1 = X[:, 1:]
print X1

distances = pdist(X1, wminkowski, 2, weights)
distance_matrix= squareform(distances)
print distance_matrix

distancelist = []
for index in range(0,17):
    distancelist.append(distance_matrix[index])
    
with open("/home/vanessa/NHRInsightFL/Playlist1DistanceMatrixsmall.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(distance_matrix)

    

# <codecell>

fig, ax = plt.subplots(1)
data = np.loadtxt(open("/home/vanessa/NHRInsightFL/Playlist1DistanceMatrixsmall.csv","rb"),delimiter=",",skiprows=1)
transformed=[]
print data[1]

for line in data:
    transline = []
    for index, bit in enumerate(line):
        transline.append(bit)
    transformed.append(transline)

        
fig, ax = ppl.subplots(1)


ppl.pcolormesh(fig, ax, data)
fig.savefig('pcolormesh_prettyplotlib_default.png')

# <codecell>

fig, ax = plt.subplots(1)
data = np.loadtxt(open("/home/vanessa/NHRInsightFL/Playlist1DistanceMatrixsmall.csv","rb"),delimiter=",",skiprows=1)
transformed=[]

print 
for line in data:
    transline = []
    for index, bit in enumerate(line):
        bity = -0.8*float(bit)+1
        #print bity
        transline.append(bity)
    transformed.append(transline)
transformed = np.array(transformed)

fig, ax = ppl.subplots(1)


ppl.pcolormesh(fig, ax, transformed)
fig.savefig('pcolormesh_prettyplotlib_default.png')

# <codecell>


