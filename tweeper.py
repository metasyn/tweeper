import requests
import tweepy, time, sys
import configparser
import json

# Load Configs
config = configparser.ConfigParser()
config.read('./tweeper.conf')

# Get our tokens & keys
HEC_TOKEN = config.get('HEC', 'HEC_TOKEN')
HEC_PORT = config.get('HEC', 'HEC_PORT')
CONSUMER_KEY = config.get('twitter', 'CONSUMER_KEY')
CONSUMER_SECRET = config.get('twitter', 'CONSUMER_SECRET')
ACCESS_KEY = config.get('twitter', 'ACCESS_KEY')
ACCESS_SECRET = config.get('twitter', 'ACCESS_SECRET')

# Get our Splunk metadata
SPLUNK_SERVER = config.get('default', 'splunk_server')
HOST = config.get('default', 'host')
SOURCE = config.get('default', 'source')
SOURCETYPE = config.get('default', 'sourcetype')

# Connect to our twitter app
auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)
api = tweepy.API(auth)

# Setup our header for the Http Event Collector (HEC)
HEADERS = {'Authorization': 'Splunk ' + HEC_TOKEN}

# Grab whatever we'd like to track on twitter
TARGETS = config.get('twitter', 'TARGETS').split(',')

# Here is where we setup the listener
# We inherit from tweepy's StreamListener class
# Inside the class, whatever we put inside on_status
# Will determine what we do with the data from the stream
class TweetStreamListener(tweepy.StreamListener):

    def on_status(self, status):

        # splunk wants to use this source so lets rename it
        status._json['tweet_source'] = status._json.pop('source')

        # url endpoint
        endpoint = '{}:{}/services/collector'.format(SPLUNK_SERVER, HEC_PORT)

        # configure basic
        data = {
            "host": HOST,
            "source": SOURCE,
            "sourcetype": SOURCETYPE,
            "event": status._json
        }

        data = json.dumps(data).encode('utf8')

        r = requests.post(
        endpoint,
        headers = HEADERS,
        data = data
        )

# test_tweet = "If we knew what it was we were doing, it would not be called research, would it? -Einstein"
# api.update_status(test_tweet)

listener = TweetStreamListener()
stream = tweepy.Stream(auth=auth, listener=listener)

stream.filter(track=TARGETS)
