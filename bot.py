import time
import tweepy
import os
import markovify
import logging
import random

from markov import langdon_generator

log = logging.getLogger("bot")
log.setLevel(logging.DEBUG)

CONSUMER_API = os.environ["CONSUMER_API_KEY"]
CONSUMER_SECRET = os.environ["CONSUMER_SECRET"]
ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
ACCESS_SECRET = os.environ["ACCESS_SECRET"]

auth = tweepy.OAuthHandler(CONSUMER_API, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

langdon_tweets = []

for tweet in tweepy.Cursor(api.user_timeline, id="iludeathmetal", tweet_mode='extended', exclude_replies=True).items(400):
    #no @'ing people
    if (not tweet.retweeted) and ('RT @' not in tweet.full_text):
        langdon_tweets.append(tweet.full_text)
api.update_status(langdon_generator(langdon_tweets))

