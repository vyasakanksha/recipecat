import plotly
import networkx as nx
import random

from plotly.graph_objs import *
from reader import init_train, build_cuisines, recipe

#G=nx.Graph()
#G.add_node('cheese')
#G.add_node('egg')
#G.add_node('lamp')

#initialize the graph with name cname and nodes ingr
def setup_graph(ingr, cname):
   # dict with random values for the position of the nodes
   p=dict((i,(random.gauss(0,2),random.gauss(0,2))) for i in range(len(ingr)))

   # creating the graph
   G = nx.empty_graph()
   G.add_nodes_from(p) 
   
   # Setting an attribute with the position of each node in the graph
   pos=nx.set_node_attributes(G,'pos', p)

   # Creating the nodes
   node_trace = Scatter(
       x=[], 
       y=[], 
       text=[],
       name = cname,
       mode='markers', 
       hoverinfo='text')

   # adding positions for the nodes
   for node in G.nodes():
       x, y = G.node[node]['pos']
       node_trace['x'].append(x)
       node_trace['y'].append(y)

   # naming the nodes
   node_trace['text'].extend(ingr)
    
   return node_trace

# Creating the visual graph
def display(data_lst):
   fig = Figure(data=Data(data_lst),
                layout=Layout(
                   title='<br>What\'s Cooking',
                   titlefont=dict(size=16),
                   showlegend=True, 
                   width=650,
                   height=650,
                   hovermode='closest',
                   margin=dict(b=20,l=5,r=5,t=40),
                   annotations=[ dict(
                       text="Python code: <a href='https://plot.ly/ipython-notebooks/network-graphs/'> https://plot.ly/ipython-notebooks/network-graphs/</a>",
                       showarrow=False,
                       xref="paper", yref="paper",
                       x=0.005, y=-0.002 ) ],
                   xaxis=XAxis(showgrid=False, zeroline=False, showticklabels=False),
                   yaxis=YAxis(showgrid=False, zeroline=False, showticklabels=False)))

   # drawing the graph
   plotly.offline.plot(fig)


