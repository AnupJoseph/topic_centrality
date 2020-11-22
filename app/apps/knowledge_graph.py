from sample_graph_maker import make_graph_parts
import igraph as ig

# Import libraries
import dash
import dash_core_components as dcc
import dash_html_components as html

import chart_studio.plotly as py
from plotly.offline import iplot
import plotly.graph_objs as go

def make_graph(nodes, edges):
    G = ig.Graph()
    for node in nodes:
        G.add_vertex(node[0], type=node[1], color=node[2])

    layout = G.layout('kk', dim=3)
    G.add_edges(edges)
    return G, layout


nodes,edges = make_graph_parts(10)
G, glayout = make_graph(nodes, edges)

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
    Xn += [glayout[k][0]]
    Yn += [glayout[k][1]]
    Zn += [glayout[k][2]]

Xe = []
Ye = []
Ze = []

for e in edges:
    # print(e)
    if e[0] is None or e[1] is None:
        pass
    else:
        # x-coordinates of edge ends
        Xe += [glayout[e[0]][0], glayout[e[1]][0], None]
        Ye += [glayout[e[0]][1], glayout[e[1]][1], None]
        Ze += [glayout[e[0]][2], glayout[e[1]][2], None]

trace1 = go.Scatter3d(x=Xe, y=Ye, z=Ze, mode='lines', line=dict(
    color='rgb(125,125,125)', width=1), hoverinfo='none')

trace2 = go.Scatter3d(x=Xn, y=Yn, z=Zn, mode='markers', name='tweets',
                      marker=dict(symbol='circle', size=6, color=group, colorscale='Viridis',
                                  line=dict(color='rgb(50,50,50)', width=0.5)), text=labels, hoverinfo='text')

axis = dict(showbackground=False, showline=False, zeroline=False,
            showgrid=False, showticklabels=False, title='')

fig_layout = go.Layout(
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

fig = go.Figure(data=data, layout=fig_layout)

layout = html.Div([
    dcc.Graph(figure=fig)
])
