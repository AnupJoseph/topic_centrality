from app import app
from app import server
from apps import knowledge_graph, dataset, home, lda_topic_dist, topic_centrality_app

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

# building the navigation bar
# https://github.com/facultyai/dash-bootstrap-components/blob/master/examples/advanced-component-usage/Navbars.py
dropdown = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem("Home", href="/"),
        dbc.DropdownMenuItem("Graph", href="/graph"),
        dbc.DropdownMenuItem("Dataset", href="/dataset"),
        dbc.DropdownMenuItem("LDA", href='/lda_results'),
        dbc.DropdownMenuItem("Topic Centrality Results",href="/topic_res")
    ],
    nav=True,
    in_navbar=True,
    label="Explore",
)

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(
                            html.Img(src="/static/election2020.png", height="30px")),
                        dbc.Col(dbc.NavbarBrand(
                            "ELECTION TWEETS DASH", className="ml-2")),
                    ],
                    align="center",
                    no_gutters=True,
                ),
                href="/",
            ),

            dbc.NavbarToggler(id="navbar-toggler2"),
            dbc.Collapse(
                dbc.Nav(
                    # right align dropdown menu with ml-auto className
                    [dropdown], className="ml-auto", navbar=True
                ),
                id="navbar-collapse2",
                navbar=True,
            ),
        ]
    ),
    color="dark",
    dark=True,
    className="mb-4",
)


def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


for i in [3]:
    app.callback(
        Output(f"navbar-collapse{i}", "is_open"),
        [Input(f"navbar-toggler{i}", "n_clicks")],
        [State(f"navbar-collapse{i}", "is_open")],
    )(toggle_navbar_collapse)

# embedding the navigation bar
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/graph':
        return knowledge_graph.layout
    elif pathname == '/dataset':
        return dataset.layout
    elif pathname == '/lda_results':
        return lda_topic_dist.layout
    elif pathname == '/topic_res':
        return topic_centrality_app.layout
    else:
        return home.layout


if __name__ == '__main__':
    app.run_server(debug=True)
