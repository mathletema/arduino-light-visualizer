# imports

import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
import time
from pprint import pprint
from time import sleep
import sys
import serial
import numpy as np

# set environmental variables
os.environ['SPOTIPY_CLIENT_ID'] = ""
os.environ['SPOTIPY_CLIENT_SECRET'] = ""
os.environ['SPOTIPY_REDIRECT_URI'] = 'http://localhost:8888/callback'

# songs to listen o

#tid = 'spotify:track:5jQI2r1RdgtuT8S3iG8zFC' #Taylor Swift
#tid = 'spotify:track:7kTVe6XhIveidvkt8nb7jK' #Gymnopedies
#tid = 'spotify:track:5u5aVJKjSMJr4zesMPz7bL' #Clair de Lune
#tid = 'spotify:track:58ge6dfP91o9oXMzq3XkIS' #505
#tid = 'spotify:track:0bYg9bo50gSsH3LtXe2SQn' #All I Want For Christmas is You
#tid = 'spotify:track:78Sw5GDo6AlGwTwanjXbGh' #Here With Me
#tid = 'spotify:track:0cgy8EueqwMuYzOZrW5vPB' #Young Gravy
#tid = 'spotify:track:6Sy9BUbgFse0n0LPA5lwy5' #Darude Sandstorm
#tid = 'spotify:track:0nF5aQoLs2YtbWwClXvumL' #bumblebee
#tid = 'spotify:track:76bzcAMft1MGxK5BCjmA0T' #Elgar Cello Concerto
#tid = 'spotify:track:3wAEhWSx5GvfCkqJ1SPA5S' #Dark Apparat
#tid = 'spotify:track:42gZM6AQ9BDMaTyTmMDVlN' #Schindler's List
#tid = 'spotify:track:61dYvvfIRtIDFuqZypPAta' #Bach Suite 1 Prelude
tid = 'spotify:track:7xoUc6faLbCqZO6fQEYprd' #One more time

# spotify
scope = "user-read-playback-state,user-modify-playback-state"
sp = spotipy.Spotify(client_credentials_manager=SpotifyOAuth(scope=scope))
analysis = sp.audio_analysis(tid)

# arduino
arduino = serial.Serial(port='COM4', baudrate=115200, timeout=.1)

# pointer to song chunk
p = 0

# start song
sp.start_playback(uris=[tid])

# start time
start = time.time()

try:
    while True:
        if (time.time() - start > analysis['segments'][p]["start"]):
            pitches = analysis['segments'][p]["pitches"]
            x = 0
            for i in range(8):
                t = pitches[i]
                t = 1 if t > 0.2 else 0
                x += t << i
            arduino.write(x.to_bytes(1, 'big'))
            
            p += 1
except:
    quit()