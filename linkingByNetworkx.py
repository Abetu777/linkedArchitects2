import networkx as nx
import pandas as pd
from pyvis.network import Network
import pickle

with open('dictArchitects.pkl', 'rb') as f:
	dictArchitects = pickle.load(f)

G = nx.Graph()
G.add_node(1)
nx.draw_circular(G)

# g = Network(notebook=True)
# g.from_nx(G)
# g.show('sample.html')