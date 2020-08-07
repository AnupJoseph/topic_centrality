import pandas as pd
import tweepy
from tweet_config import api,COLS
from preprocess import cleaner
import os
from datetime import datetime
import tqdm

startDate = datetime(2020, 8, 6, 0, 0, 0)
EndDate = datetime(2020, 8, 7, 0, 0, 0)


def get_tweets(screen_name,latest_date_found=None,en_only=True):
	print(f"Returning Tweets for {screen_name}")
	tweets = tweepy.Cursor(api.user_timeline,screen_name=screen_name,include_rts=False,tweet_mode='extended')
	timeline_df = pd.DataFrame(columns=COLS)

	print(f"Cleaning Data")

	pbar = tqdm.tqdm(iterable=timeline_df[:5])
	for tweet in tweets.items():
			if ((en_only and tweet.lang == 'en') or not en_only) and (tweet.created_at<EndDate and tweet.created_at>EndDate):
					tweet_df = cleaner(tweet)
					timeline_df = timeline_df.append(tweet_df,ignore_index = True)
					pbar.update(1)
	pbar.close()

	if latest_date_found:
		print("-- Removing dates before {} -- ".format(latest_date_found))
		timeline_df['to_date'] = pd.to_datetime(timeline_df['created_at']).dt.tz_convert(None)
		timeline_df = timeline_df[timeline_df['to_date'] > latest_date_found]
		timeline_df.drop('to_date',axis=1)

	return timeline_df

def write_to_file(file_location,tweets_df):
	csvFile = open(file_location, 'w+' ,encoding='utf-8')
	tweets_df.to_csv(csvFile, mode='w+', index=False, encoding="utf-8")

def combine_tweets(user_name,en_only=False):
	file_location = "data/{}_data.csv".format(user_name)
	latest_date_found = None
	old_data = None

	if os.path.exists(user_name):
		old_data = pd.read_csv(file_location)
		dates_series = pd.to_datetime(old_data['created_at']).dt.tz_convert(None)
		latest_date_found = dates_series.max()
		tweets_df = get_tweets(user_name,latest_date_found,en_only) 
		new_tweets_count = tweets_df.shape[0]
		tweets_df = tweets_df.append(old_data,sort=False)
		print("Total_tweets = {}; New tweets added for {} = {}".format(tweets_df.shape[0],user_name,new_tweets_count))
		write_to_file(file_location,tweets_df)
	else:
		tweets_df = get_tweets(user_name,latest_date_found,en_only)
		write_to_file(file_location,tweets_df)


user_names = ["SenSanders","realDonaldTrump"]
for user_name in user_names:
	combine_tweets(user_name,en_only = True)