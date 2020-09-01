# External Imports
import pandas as pd

# Internal imports
from tweepy_config import RETWEET_COLS

def merger(screen_name,data_frame):
    """Merge the new dataframe with the prexisting file

    Args:
        screen_name ([string]): use name of the politicians
        data_frame ([pandas.Dataframe]): new set of retweets to be appended to the existing file
    """
    final_csv = f'../data/{screen_name}/{screen_name}_retweets.csv'
    with open(final_csv, 'a') as f:
        data_frame.to_csv(f, header=f.tell()==0,columns=RETWEET_COLS)

def write_to_file(file_path,new_data,screen_name):
    merger(screen_name,new_data)