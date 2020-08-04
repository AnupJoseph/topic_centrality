import pandas as pd
import tweepy
from tweet_config import api,COLS
from preprocess import preprocesss

def get_tweets(screen_name):
	"""Function to get tweets of a specific user
	
	Args:
	    screen_name (string):User name under consideration  
	"""
	print(f"Returning Tweets for {screen_name}")
	tweets = tweepy.Cursor(api.user_timeline,screen_name=screen_name,include_rts=False,tweet_mode='extended')
	# tweets_df = pd.DataFrame(columns=COLS)
	i=0
	for tweet in tweets.items():

		tweet = tweet._json
		raw_text = preprocesss(tweet['full_text'])
		print(raw_text+'\n')
		if i>5:
			break
		i+=1
	# print(tweets)

get_tweets("SenSanders")