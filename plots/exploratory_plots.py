import pandas as pd
import plotly


# from data_collection_processing import tweepy_config
# RETWEET_COLS = ['original_tweet_id', 'retweet_id', 'type', 'created_at',
#                 'source', 'favorite_count', 'retweet_count', 'original_author']
politicians = ['SenSanders', 'realDonaldTrump', 'JoeBiden', 'andrewcuomo', 'TeamPelosi',
               'NikkiHaley', 'MittRomney', 'Mike_Pence', 'SenatorCollins', 'PeteButtigieg']

def save_to_excel(dataframe_list,outfolder= 'excels'):
    import os
    if not os.path.exists(outfolder):
        os.makedirs(outfolder)
    writer = pd.ExcelWriter('Combined_politicians_list.xlsx', engine='xlsxwriter')
    for index,tables in enumerate(dataframe_list):
        tables.to_excel(writer,sheet_name=politicians[index])
    writer.save()

frames = []
for politician in politicians:
    file_path = f"../data/{politician}/{politician}_data.csv"
    dataframe = pd.read_csv(file_path)
    dataframe['Date'] = pd.to_datetime(dataframe['created_at']).dt.date
    dataframe = dataframe[['created_at','Date']]
    dataframe = dataframe.groupby('Date').count()
    frames.append(dataframe)

save_to_excel(frames,'trends')