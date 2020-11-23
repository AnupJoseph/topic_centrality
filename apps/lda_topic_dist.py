import plotly.graph_objects as go
import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc


from .calculate_percentage import calculate_percentage
def topic_fig(series,n):
    labels = [f'Topic {i}' for i in range(n)]
    fig = go.Figure(data=[go.Pie(labels=labels, values=percentages, hole=0.6)])
    fig.update_traces(textposition='outside', textinfo='percent+label')
    return fig

from .calculate_tweets import calculate_tweets
def tweet_topic_fig(leader_dataframe,n):
    colors = {
        0:'#003f5c',
        1:'#58508d',
        2:'#bc5090',
        3:'#ff6361',
        4:'#ffa600'
    }
    fig = go.Figure()
    labels = [f'Topic {i}' for i in range(n)]
    for index,leader in enumerate(leader_dataframe.columns):
        fig.add_trace(go.Bar(x=labels,
                y=leader_dataframe[leader],
                name=leader,
                marker_color=colors[index]
                ))
    fig.update_layout(
    title='US Export of Plastic Scrap',
    xaxis_tickfont_size=14,
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1)
    return fig

percentages = calculate_percentage()
leader_dataframe = calculate_tweets(7)
layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1(children='Topic distribution in tweets at a glance'),
                className="mb-6")
    ])
    ]),
    dbc.Row([
        dcc.Graph(figure=topic_fig(percentages,7))
    ]),
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1(children='Topic distribution by leader in tweets at a glance'),
                className="mb-6")
    ])
    ]),
    dbc.Row([
        dcc.Graph(figure=tweet_topic_fig(leader_dataframe,7))
    ]),
])
