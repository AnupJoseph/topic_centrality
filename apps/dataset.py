import dash_table
import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

df = pd.read_csv(
    'https://raw.githubusercontent.com/AnupJoseph/topic_centrality/master/data/sparkling_clean_data.csv')
df = df.sample(100)

df2 = pd.read_csv(
    'https://raw.githubusercontent.com/AnupJoseph/topic_centrality/master/data/combined_dataframe.csv')
df = df.sample(100)
layout = html.Div([
    dbc.Container([
        dash_table.DataTable(
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
        ),
        dbc.Col(
            html.H1(children='Topic centrality distribution by sum', className="mb-6")),
        dash_table.DataTable(
            style_cell={
                'overflow': 'hidden',
                'textOverflow': 'ellipsis',
                'maxWidth': 0,
            },
            id='table',
            columns=[{"name": i, "id": i} for i in df.columns],
            data=df2.to_dict("rows"),
            tooltip_data=[
                {
                    column: {'value': str(value), 'type': 'markdown'}
                    for column, value in row.items()
                } for row in df2.to_dict('rows')
            ],
            tooltip_duration=None
        )
    ])
])
