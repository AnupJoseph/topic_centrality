import pandas as pd
from tweepy_config import RETWEET_COLS

def merger(screen_name,data_frame):
	final_csv = f'../data/{screen_name}/{screen_name}_retweets.csv'
	# df = pd.read_csv(file_path)
	with open(final_csv, 'a') as f:
		data_frame.to_csv(f, header=f.tell()==0,columns=RETWEET_COLS)
def write_to_file(file_path,new_data,screen_name):
	"""
		Writes a dataframe to file
	"""
	data_frame = new_data
	# csvFile = open(file_path, 'w' ,encoding='utf-8')
	# data_frame.to_csv(csvFile, mode='w', index=False, encoding="utf-8")
	merger(screen_name,data_frame)
