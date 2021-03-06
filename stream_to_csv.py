import json
import pandas as pd
import csv
from twython import Twython
from twython import TwythonStreamer
import time

# Load credentials from json file
with open("twitter_credentials.json", "r") as file:
    creds = json.load(file)

# Filter out unwanted data
def process_tweet(tweet):
    d = {}
    d['hashtags'] = [hashtag['text'] for hashtag in tweet['entities']['hashtags']]
    d['text'] = tweet['text']
    d['user'] = tweet['user']['screen_name']
    d['user_loc'] = tweet['user']['location']
    return d

# Filter out unwanted data
def print_to_term(tweet):
    d = {}
    d['text'] = tweet['text']
    return print (d)

# Create a class that inherits TwythonStreamer
class MyStreamer(TwythonStreamer):

    # Received data
    def on_success(self, data):
        # Only collect tweets in English
        # if data['lang'] == 'en':
        # tweet_data = process_tweet(data)
        try:
            print_to_term(data)
        except:
            pass
        try:
            self.save_to_csv(data)
        except:
            pass

    # Problem with the API
    def on_error(self, status_code, data):
        print(status_code, data)
        self.disconnect()
        
    # Save each tweet to csv file
    def save_to_csv(self, tweet):
        with open(r'saved_tweets.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow(list(tweet.values()))

def start_stream(keyword):
    return stream.statuses.filter(track=keyword)

# Instantiate from our streaming class
stream = MyStreamer(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'], 
                    creds['ACCESS_TOKEN'], creds['ACCESS_SECRET'])
# Start the stream
# stream.statuses.filter(track='corona')
start_stream('corona')