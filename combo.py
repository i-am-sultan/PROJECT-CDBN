from cdlib import algorithms
import networkx as nx
G = nx.karate_club_graph()
coms = algorithms.pycombo(G)