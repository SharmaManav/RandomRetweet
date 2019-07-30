import requests
import json
import tweepy
import random
import config

auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_SECRET)

api = tweepy.API(auth)

tweetID = input("What's the tweet ID? ")

tweet_retweets = api.retweeters(id = tweetID, stringify_ids = 'true')
	
winner = (tweet_retweets[(random.randrange(0, len(tweet_retweets)-1))])
winnerUsername = api.get_user(id = winner);
print("random retweet ID : ", winner)
print("User is: ", winnerUsername.screen_name)