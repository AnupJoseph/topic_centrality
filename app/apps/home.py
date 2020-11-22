  
import dash_html_components as html
import dash_bootstrap_components as dbc

# needed only if running this as a single page app
#external_stylesheets = [dbc.themes.LUX]

#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# change to app.layout if running as single page app instead
layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1("Welcome to the Election 2020 dashboard", className="text-center")
                    , className="mb-5 mt-5")
        ]),
        dbc.Row([
            dbc.Col(html.H5(children='This app marks my very first attempt at using Plotly, Dash and Bootstrap! '
                                     )
                    , className="mb-4")
            ]),

        dbc.Row([
            dbc.Col(html.H5(children='This is just a cool looking dash board')
                    , className="mb-5")
        ]),

        dbc.Row([
            dbc.Col(dbc.Card(children=[html.H3(children='Get the original datasets used in this dashboard',
                                               className="text-center"),
                                       dbc.Row([dbc.Col(dbc.Button("Tweets", href="https://github.com/AnupJoseph/topic_centrality/blob/master/data/sparkling_clean_data.csv",
                                                                   color="primary"),
                                                        className="mt-3"),
                                                dbc.Col(dbc.Button("Singapore", href="https://github.com/AnupJoseph/topic_centrality/blob/master/data/combined_dataframe.csv",
                                                                   color="primary"),
                                                        className="mt-3")], justify="center")
                                       ],
                             body=True, color="dark", outline=True)
                    , width=4, className="mb-4"),

            dbc.Col(dbc.Card(children=[html.H3(children='Access the code used to build this dashboard',
                                               className="text-center"),
                                       dbc.Button("GitHub",
                                                  href="https://github.com/AnupJoseph/topic_centrality",
                                                  color="primary",
                                                  className="mt-3"),
                                       ],
                             body=True, color="dark", outline=True)
                    , width=4, className="mb-4"),

            dbc.Col(dbc.Card(children=[html.H3(children='Read the original research paper',
                                               className="text-center"),
                                       dbc.Button("Paper",
                                                  href="https://github.com/cameron-raymond/CISC500-SeniorThesis/blob/master/CRaymond_Undergraduate_Thesis.pdf",
                                                  color="primary",
                                                  className="mt-3"),

                                       ],
                             body=True, color="dark", outline=True)
                    , width=4, className="mb-4")
        ], className="mb-5"),

        # html.A("Special thanks to Flaticon for the icon in COVID-19 Dash's logo.",
        #        href="https://www.flaticon.com/free-icon/coronavirus_2913604")

    ])

])
