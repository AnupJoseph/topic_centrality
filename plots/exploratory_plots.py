import pandas as pd
import plotly


# from data_collection_processing import tweepy_config
# RETWEET_COLS = ['original_tweet_id', 'retweet_id', 'type', 'created_at',
#                 'source', 'favorite_count', 'retweet_count', 'original_author']
politicians = ['SenSanders', 'realDonaldTrump', 'JoeBiden', 'andrewcuomo', 'TeamPelosi',
               'NikkiHaley', 'MittRomney', 'Mike_Pence', 'SenatorCollins', 'PeteButtigieg']


frames = []
for politician in politcians:
    file_path = f"../data/{politician}/{politician}_data.csv"
    timeline_df = pd.read_csv(file_path)
    frames.append(timeline_df)
total_df = pd.concat(frames,sort=False)  

total_df["Date"] = pd.to_datetime(total_df['created_at']).dt.date
tweets_over_time = total_df[["Date","created_at","original_author"]]
tweets_over_time["Cumulative"] = total_df["created_at"]
tweets_over_time = tweets_over_time.drop("created_at",axis=1)
tweets_over_time = tweets_over_time.groupby(tweets_over_time["Date"]).count()

tweets_over_time.to_csv('final.csv')
cumulative_tweets = tweets_over_time["Cumulative"].cumsum()

cumulative_tweets.to_csv('cumul_final.csv')