import dash
import dash_table
import pandas as pd

df = pd.read_csv('https://github.com/AnupJoseph/topic_centrality/blob/master/data/sparkling_clean_data.csv')
layout = dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.to_dict("rows"),
)