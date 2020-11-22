import pandas as pd
import collections
def make_graph_parts(n):
    politicians = ['SenSanders', 'realDonaldTrump', 'JoeBiden', 'andrewcuomo', 'TeamPelosi',
                   'NikkiHaley', 'MittRomney', 'Mike_Pence', 'SenatorCollins', 'PeteButtigieg']
    COLS = ['id', 'created_at', 'original_text', 'clean_text',
            'retweet_count', 'hashtags', 'mentions', 'original_author']
    RETWEET_COLS = ['original_tweet_id', 'retweet_id', 'type', 'created_at',
                    'source', 'favorite_count', 'retweet_count', 'original_author']
    graph_dict = dict(zip(politicians, range(len(politicians))))
    tweets_dict = collections.defaultdict(str)

    config_dict = {
        'colours': ['firebrick','orange','violet' ]
    }
    print(config_dict['colours'])

    nodes = []

    for index, p in enumerate(politicians):
        nodes.append([index, p, 'politician', config_dict['colours'][0]])

    tweets_df = pd.DataFrame(columns=COLS)
    retweets_df = pd.DataFrame(columns=RETWEET_COLS)
    for politician in politicians:
        twitter_df = pd.read_csv(
            f"../data/{politician}/{politician}_data.csv")
        if n:
            twitter_df = twitter_df.sample(
                n=min(n, len(twitter_df)), random_state=1)
        tweets_df = pd.concat([tweets_df, twitter_df])

        retweet_data = pd.read_csv(
            f"../data/{politician}/{politician}_retweets.csv")
        # if we're only taking 20 tweets find all the retweets for those 20
        retweet_data = retweet_data[retweet_data['original_tweet_id'].isin(
            twitter_df['id'])]
        retweet_data = retweet_data.sample(n*2)
        retweets_df = pd.concat([retweets_df, retweet_data])

    tweets_df['no'] = range(len(tweets_df))
    tweets_df.set_index('no', inplace=True)

    edges = []
    index = 10
    for row in tweets_df.index:
        tweets_dict[str(tweets_df['id'][row])] = index
        nodes.append([index, (str(tweets_df['id'][row]),
                              tweets_df['original_text'][row]), 'tweet', config_dict['colours'][1]])

        edges.append((graph_dict[tweets_df['original_author'][row]], index))
        index += 1

    retweets_df['no'] = range(len(retweets_df))
    retweets_df.set_index('no', inplace=True)

    i = 0
    for row in retweets_df.index:
        nodes.append([index, (retweets_df['retweet_id'][row],
                              retweets_df['original_author'][row]), 'retweet', config_dict['colours'][2]])
        source = None
        if str(retweets_df['original_tweet_id'][row]) in tweets_dict.keys():
            source = tweets_dict[str(retweets_df['original_tweet_id'][row])]
        if source is None:
            pass
        else:
            edges.append((source, index))
            index += 1
    
    return nodes,edges