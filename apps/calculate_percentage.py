import pandas as pd 
from collections import Counter
import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

def calculate_percentage():
    politicians = ['SenSanders', 'realDonaldTrump', 'JoeBiden', 'andrewcuomo', 'TeamPelosi',
                   'NikkiHaley', 'MittRomney', 'Mike_Pence', 'SenatorCollins', 'PeteButtigieg']
    COLS = ['id', 'created_at', 'original_text', 'clean_text',
            'retweet_count', 'hashtags', 'mentions', 'original_author']

    data = pd.DataFrame(columns=COLS)
    for politician in politicians:
        df = pd.read_csv(f"data/{politician}/{politician}_data_temp.csv")
        # df.drop(labels=['Unnamed: 0','Unnamed: 0.1'],inplace=True)
        df.drop('Unnamed: 0',inplace=True,axis=1)
        df.drop('Unnamed: 0.1',inplace=True,axis=1)
        data = pd.concat([data,df])
    
    percentage_data = Counter(data['lda_cluster'])

    total = sum(percentage_data.values())
    return[(item/total)*100 for item in percentage_data.values()]
        