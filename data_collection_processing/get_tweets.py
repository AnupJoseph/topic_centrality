# External Imports
import pandas as pd
import GetOldTweets3 as got

# Internal imports
from tweepy_config import COLS,politicians
from preprocess import cleaner

def get_tweets(screen_name,start_date,end_date):
    """Function to collect all the tweets of a politician and perform the preprocessing pipeline on the tweets

    Args:
        screen_name ([string]): User name of the politician
        start_date ([string]): starting date from which the tweets are to be collected
        end_date ([string]): Ending date upto which the tweets are to be collected
    """

    print(f"Getting tweets of {screen_name}")

    # Set the criteria for tweets are gather them
    tweet_criteria = got.manager.TweetCriteria().setUsername(screen_name).setSince(start_date)\
    .setUntil(end_date).setEmoji('unicode')
    tweets = got.manager.TweetManager.getTweets(tweet_criteria)

    # Dump the tweets into a dataframe and send the dataframe for preprocessing
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
