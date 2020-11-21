# Import libraries
import dash
import dash_core_components as dcc
import dash_html_components as html

import chart_studio.plotly as py
from plotly.offline import iplot
import plotly.graph_objs as go

import igraph as ig

from sample_graph_maker import make_graph_parts


def make_graph(nodes, edges):
    G = ig.Graph()
    # print(edges)
    # print(nodes)
    for node in nodes:
        G.add_vertex(node[0], type=node[1], color=node[2])
    layout = G.layout('grid_3d', dim=3)
    G.add_edges(edges)
    return G, layout


nodes,edges = make_graph_parts(10)
G, layout = make_graph(nodes, edges)

labels = []
group = []
types = []

for node in nodes:
    if node[2] != 'politician':
        labels.append('<br>'.join(str(i) for i in node[1]))
    else:
        labels.append(node[1])
        types.append(node[2])
        group.append(node[3])

Xn = []
Yn = []
Zn = []

for k in range(len(nodes)):
    Xn += [layout[k][0]]
    Yn += [layout[k][1]]
    Zn += [layout[k][2]]

Xe = []
Ye = []
Ze = []

for e in edges:
    # print(e)
    if e[0] is None or e[1] is None:
        pass
    else:
        # x-coordinates of edge ends
        Xe += [layout[e[0]][0], layout[e[1]][0], None]
        Ye += [layout[e[0]][1], layout[e[1]][1], None]
        Ze += [layout[e[0]][2], layout[e[1]][2], None]

trace1 = go.Scatter3d(x=Xe, y=Ye, z=Ze, mode='lines', line=dict(
    color='rgb(125,125,125)', width=1), hoverinfo='none')

trace2 = go.Scatter3d(x=Xn, y=Yn, z=Zn, mode='markers', name='tweets',
                      marker=dict(symbol='circle', size=6, color=group, colorscale='Viridis',
                                  line=dict(color='rgb(50,50,50)', width=0.5)), text=labels, hoverinfo='text')

axis = dict(showbackground=False, showline=False, zeroline=False,
            showgrid=False, showticklabels=False, title='')

layout = go.Layout(
    title="Network of tweets for American election",
    width=1000,
    height=1000,
    showlegend=False,
    scene=dict(
        xaxis=dict(axis),
        yaxis=dict(axis),
        zaxis=dict(axis),
    ))

data = [trace1, trace2]

fig = go.Figure(data=data, layout=layout)
# fig.show()
# iplot(fig, filename='Netwrok grapg')


# Create the app
app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

app.run_server(debug=True, use_reloader=False)
