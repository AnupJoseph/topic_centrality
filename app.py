import dash
import dash_bootstrap_components as dbc
import os

from flask import Flask
import flask
# bootstrap theme
# https://bootswatch.com/lux/
external_stylesheets = [dbc.themes.LUX]

STATIC_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
server = Flask(__name__)

app = dash.Dash(__name__, external_stylesheets=external_stylesheets,server=server)

@app.server.route('/static/<resource>')
def serve_static(resource):
    return flask.send_from_directory(STATIC_PATH, resource)


# server = app.server
app.config.suppress_callback_exceptions = True