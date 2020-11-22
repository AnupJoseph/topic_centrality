import dash
import dash_table
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/AnupJoseph/topic_centrality/master/data/sparkling_clean_data.csv')
layout = dash_table.DataTable(
    style_cell={
        'overflow': 'hidden',
        'textOverflow': 'ellipsis',
        'maxWidth': 0,
    },
    id='table',
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.to_dict("rows"),
    tooltip_data=[
        {
            column: {'value': str(value), 'type': 'markdown'}
            for column, value in row.items()
        } for row in df.to_dict('rows')
    ],
    tooltip_duration=None
)