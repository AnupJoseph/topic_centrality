import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import pandas as pd
from collections import Counter
import operator

def calculate_tweets(n):
    politicians = ['SenSanders', 'realDonaldTrump', 'JoeBiden', 
    # 'andrewcuomo', 'TeamPelosi','NikkiHaley', 'MittRomney', 
                   'Mike_Pence', 
                #    'SenatorCollins', 
                   'PeteButtigieg']
    dataset = pd.DataFrame(index=range(-1,n))

    # for i in range(n):
    for politician in politicians:
        df = pd.read_csv(f"data/{politician}/{politician}_data_temp.csv")
        data = Counter(df['lda_cluster'])
        data = [(key,value) for key,value in data.items()]
        data = sorted(data,key=operator.itemgetter(0))
        dataset[politician] = pd.DataFrame([i[1] for i in data],index=[i[0] for i in data])
    
    return dataset
        