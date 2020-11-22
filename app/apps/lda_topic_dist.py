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


percentages = calculate_percentage()
layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1(children='Topic distribution in tweets at a glance'),
                className="mb-6")
    ])
    ]),
    dbc.Row([
        dcc.Graph(figure=topic_fig(percentages,7))
    ])

])
