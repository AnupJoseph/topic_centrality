# System imports
import math
import os

# External Imports
import pandas as pd

# Internal imports
from tweepy_config import COLS,politicians

def split_csv_files(screen_name,size=300,index=False):
    """A utility function to split the massive tweet files into pieces of 300 lines and then add to the folder as {leader_name}/{leader_name}_{i}.csv

    Args:
        screen_name ([string]): User name of the politicians on twitter
        size (int, optional): Size as per which the file is to be split. Defaults to 300.
        index (bool, optional): Row index for the file. Defaults to False.
    """
    input_file = f'../data/{screen_name}_data.csv'
    df = pd.read_csv(input_file)
    low = 0
    high = size
    
    CHECK_DIR = os.path.isdir(f'../data/{screen_name}')
    if not CHECK_DIR:
        os.mkdir(f'../data/{screen_name}')
        
    for i in range(math.ceil(len(df)/size)):
        output_file = f'../data/{screen_name}/{screen_name}_data_{i}.csv'
        df[low:high].to_csv(output_file,index=index,columns=COLS)
        
    low = high
    if (high+size < len(df)):
        high = high + size
    else:
        high = len(df)

for screen_name in politicians:
    split_csv_files(screen_name)
