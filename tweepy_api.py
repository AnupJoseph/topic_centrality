import tweepy

from tweet_config import api

def get_tweets(screen_name):
	"""Function to get tweets of a specific user
	
	Args:
	    screen_name (string):User name under consideration  
	"""
	print(f"Returning Tweets for {screen_name}")
	tweets = tweepy.Cursor(api.user_timeline,screen_name=screen_name,include_rts=False,tweet_mode='extended')
	print(tweets)

get_tweets("SenSanders")