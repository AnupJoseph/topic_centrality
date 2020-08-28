import sys
import os
import tqdm
import tweepy
import pandas as pd
from datetime import datetime, date
from tweepy_config import * 
from write_to_file import write_to_file



class Retweet_Grabber(object):
	def __init__(self, screen_name,input_file, *args, **kwargs):
		self.__START_DATE = date(2018, 10, 21)
		self.__END_DATE =   date(2020, 1, 1)
		self.screen_name = screen_name	
		self.input_file = input_file
		self.file_path =  "../data/{}/{}_retweets.csv".format(screen_name,input_file)
		self.tweet_ids, self.retweet_df, self.num_tweets = self.get_old_retweets()	

	def get_old_retweets(self):
		# tweet_file_path		= "../data/{}_data.csv".format(self.screen_name)
		tweet_file_path = f"../data/{self.screen_name}/{self.input_file}"
		print(tweet_file_path)
		assert os.path.exists(tweet_file_path), "Tweets must be collected and placed in /data folder before retweets can be collected."
		tweet_df = pd.read_csv(tweet_file_path)
		exists = os.path.exists(self.file_path)
		old_retweets = pd.DataFrame(columns=RETWEET_COLS)
		if exists:
			total_tweets = tweet_df.shape[0]
			old_retweets = pd.read_csv(self.file_path)
			already_collected = pd.merge(tweet_df, old_retweets, how='inner', left_on='id', right_on='original_tweet_id')["id"].unique()
			to_collect = tweet_df[~tweet_df["id"].isin(old_retweets["original_tweet_id"])].dropna()
			print("--- {}: total tweets. {} retweets already collected, only collecting {} now ---".format(total_tweets,len(already_collected),to_collect.shape[0]))		
			return to_collect,old_retweets,to_collect.shape[0]
		num_tweets = tweet_df.shape[0]
		return tweet_df,old_retweets,num_tweets

	def put_tweets(self):
		screen_name = self.screen_name
		self.get_user_retweets()
		self.retweet_df["date"] = pd.to_datetime(self.retweet_df['created_at']).dt.date
		self.retweet_df = self.retweet_df[self.retweet_df["date"] >= self.__START_DATE]
		self.retweet_df = self.retweet_df.drop("date",axis=1)
		write_to_file(self.file_path,self.retweet_df,self.screen_name)
		print("--- done for {} ---".format(screen_name))

	def get_user_retweets(self):
		screen_name = self.screen_name
		index = 1
		pbar = tqdm.tqdm(total=len(self.tweet_ids))
		for _, row in self.tweet_ids.iterrows():
			tweet_id = row['id']
			retweets = self.get_retweets(tweet_id)
			self.retweet_df = self.retweet_df.append(retweets)
			if index % 74 == 0:
				print("\t> writing tweets")
				write_to_file(self.file_path,self.retweet_df,self.screen_name)
			index += 1
			pbar.update(1)
		pbar.close()
		self.retweet_df.drop(self.retweet_df.loc[self.retweet_df['original_author']==screen_name].index, inplace=True)
	
	def get_retweets(self,tweet_id):
		tweets 		= api.retweets(id=tweet_id,tweet_mode='extended')
		retweet_df = pd.DataFrame(columns=RETWEET_COLS)
		for tweet in tweets:
			tweet_df 	= self.clean_retweet(tweet,tweet_id)
			retweet_df = retweet_df.append(tweet_df, ignore_index=True)
		return retweet_df

	def clean_retweet(self,tweet_obj,tweet_id):
		cleaned_tweet 	= []
		tweet			= tweet_obj._json
		cleaned_tweet 	+= [tweet_id,tweet['id'],'retweet', tweet['created_at'],tweet['source'],tweet['favorite_count'], tweet['retweet_count']]
		cleaned_tweet.append(tweet['user']['screen_name'])
		single_tweet_df = pd.DataFrame([cleaned_tweet], columns=RETWEET_COLS)
		return single_tweet_df

if __name__ == '__main__':
	usernames = ['SenSanders']
	i = 3
	input_file = f'{usernames[0]}'+f'_data_{i}.csv'
	for username in usernames:
		print("--- starting data collection for {}".format(username))
		user = Retweet_Grabber(username,input_file)
		user.put_tweets()