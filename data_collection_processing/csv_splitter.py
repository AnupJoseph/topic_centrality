from tweepy_config import COLS,politicians
import pandas as pd
import math
import os

def split_csv_files(screen_name,size=300,index=False):
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

for name in politicians:
  split_csv_files(name)