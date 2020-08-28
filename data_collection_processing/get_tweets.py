# External module Imports
import GetOldTweets3 as got 
import pandas as pd

# Internal Module Imports
from preprocess import cleaner
from tweepy_config import COLS,politicians

def get_tweets(screen_name,start_date,end_date):
    """
    If you read this Samuel and its not working for mare than some time then set up a rolling loop 
    which will run through a certain interval of time for a user.And then append it to the existing tweets.
    A month seems to be working at the time of writing. 
    
    Args:
        screen_name (TYPE): Description
        start_date (TYPE): Description
        end_date (TYPE): Description
    """
    print(f"Getting tweets of {screen_name}")
    tweet_criteria = got.manager.TweetCriteria().setUsername(screen_name).setSince(start_date)\
    .setUntil(end_date).setEmoji('unicode')
    tweets = got.manager.TweetManager.getTweets(tweet_criteria)
    tweets_df = pd.DataFrame(columns = COLS)
    print(f"Preprocessing tweets of {screen_name}")
    for tweet in tweets:
        if tweet.text !='':
            cleaned_tweet = cleaner(tweet)
            tweets_df.loc[len(tweets_df)] = cleaned_tweet
    print(tweets_df.loc[len(tweets_df) - 1])

    print(f"Writing tweets of {screen_name}")

    tweets_df.to_csv(f'../data/{screen_name}_data.csv')
    print(f"{screen_name} work done")

for politician in politicians:
    get_tweets(politician, '2019-05-01', '2020-08-15')
