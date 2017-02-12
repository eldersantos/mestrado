from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from datetime import datetime
import tweepy
import sys
import webbrowser
import os
import requests
import json
import io
import datetime
from time import sleep
import pymongo
from pymongo import MongoClient
from RepeatedTimer import RepeatedTimer


'''
You need a MongoDb instance up and running
with a database called omni and a collection called twitterData
obviouslly we can change those name appropriately to your case
'''

# Twitter credentials
access_token = '' # Put here your access_token
access_token_secret = '' # Put here your secret token
consumer_key = '' # Put here your consumer key
consumer_secret = '' Put here your consumer secret

class StdOutListener(StreamListener):
    ''' Handles data received from the stream. '''

    
    def __init__(self, api=None):
        super(StdOutListener, self).__init__()
        self.num_tweets = 0
        self.db = connectToMongo() 
        self.collection = self.db.twitterData
        self.shouldStop = False
        self.unDesirableCities = ['New York', 'Nueva York', 'Nova Iorque', 'Queens', 'Jersey City', 'New Jersey']

    def on_data(self, data):
        try:
            tweet = json.loads(data)
            # Ignore the tweet if the place attribute is marked from one of the cities we do not want to track
            if tweet['place']['name'] in self.unDesirableCities:
                return True

            if tweet['coordinates'] is None:

                #Manhatttan point
                x = -73.98536
                y = 40.74843
                geo = tweet['place']['bounding_box']['coordinates'][0]
                poly = [(geo[0][0],geo[0][1]),(geo[1][0],geo[1][1]),(geo[2][0],geo[2][1]),(geo[3][0],geo[3][1])]
            else:
                x = tweet['coordinates']['coordinates'][0]
                y = tweet['coordinates']['coordinates'][1]
                poly = [(-74.042753,40.701265),(-73.937645,40.878805),(-73.909878,40.795327),(-73.979347,40.706887)]

            #Check if the tweet is inside the desirable polygon
            if point_inside_polygon(x,y,poly):
                tweet['_datetime'] = datetime.datetime.utcnow()
                id = self.collection.insert(tweet, continue_on_error=True)
                print(str(id))

            if self.shouldStop == True:
                return False
            else:
                return True
        except pymongo.errors.DuplicateKeyError:
            pass
            return True
        except Exception as e:
            pass
            return True

    def stop(self):
        self.shouldStop = True
 
    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True # To continue listening
 
    def on_timeout(self):
        print('Timeout...')
        return True # To continue listening
 
def point_inside_polygon(x,y,poly):

    n = len(poly)
    inside =False

    p1x,p1y = poly[0]
    for i in range(n+1):
        p2x,p2y = poly[i % n]
        if y > min(p1y,p2y):
            if y <= max(p1y,p2y):
                if x <= max(p1x,p2x):
                    if p1y != p2y:
                        xinters = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x,p1y = p2x,p2y
    return inside


def connectToMongo():
    client = MongoClient('localhost', 27017)
    ohmniDB = client['ohmni']
    return ohmniDB

def getApi():
    # OAuth process, using the keys and tokens
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    twitApi = tweepy.API(auth)
    return twitApi

def getOAuth():
    # OAuth process, using the keys and tokens
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return auth

def testTwitterApi():
    api = getApi()
    user = api.me()

    print('Name: ' + user.name)
    print('Location: ' + user.location)
    print('Friends: ' + str(user.friends_count))



if __name__ == '__main__':
    
    try:

        oauth = getOAuth()
        listener = StdOutListener()
        stream = Stream(oauth, listener)
        
        try:
            stream.filter(locations=[-74.042753,40.701265,-73.909878,40.795327]) # Manhatan
        except AttributeError:
            pass


    except KeyboardInterrupt, e:
        listener.stop()
        print('')
        print('Closing Data Collector for Twitter...')
        stream.disconnect()
        sys.exit(0)
