import plotly.graph_objects as go
import pandas as pd

import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

# layout = html.Iframe(src="static/ldaviz.html",height=525, width="100%",seamless="seamless")

layout = html.Div([
    dbc.Container([
        dbc.Row([
            html.H1(children='Topic centrality distribution by sum', className="mb-6")
        ]),
        dbc.Row([
            html.Iframe(
            src="static/Overall Importance of Topic Importance of Topic to Individual (mean).html", height=800, width="100%"),
        ]),
        dbc.Row([
            html.Iframe(
            src="static/Overall Expanded Importance of Topic Importance of Topic to Individual (mean).html", height=800, width="100%"),
        ])
    ])
])
