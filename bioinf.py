#our project

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random

# creating a graph
G = nx.erdos_renyi_graph(100, 0.1)
num_nodes=100

# initialisation (0 - healthy, 1 - infected, 2 - recovered, 3 - dead, 4 - can't get sick, 5-born)
for node in G.nodes:
    G.nodes[node]['status'] = 0

# choose random
patient_zero = random.choice(list(G.nodes))
G.nodes[patient_zero]['status'] = 1

# function for our infection
def spread_infection(G):
    for node in G.nodes:
        if G.nodes[node]['status'] == 1:  # If the vertex is infected
            neighbors = list(G.neighbors(node))
            for neighbor in neighbors:
                if G.nodes[neighbor]['status'] == 0 and np.random.rand() < 0.02:  # Probability of infection
                    G.nodes[neighbor]['status'] = 4
                if G.nodes[neighbor]['status'] == 0 and np.random.rand() < 0.3:  # Probability of infection
                    G.nodes[neighbor]['status'] = 1



# function of return
def cure_infected(G):
   for node in G.nodes:
       if G.nodes[node]['status'] == 1: # Если вершина инфицирована
           if np.random.rand() < 0.1: # Вероятность умереть
               G.nodes[node]['status'] = 3
       if G.nodes[node]['status'] == 1: # Если вершина инфицирована
           if np.random.rand() < 0.01: # Вероятность выздоровления
               G.nodes[node]['status'] = 2
       if G.nodes[node]['status'] == 2: # Если вершина выздоровела
           if np.random.rand() < 0.1: # Вероятность заболеть снова
               G.nodes[node]['status'] = 1

# animation of our infection's power
def add_new_nodes(G, num_nodes):
   for _ in range(num_nodes-(num_nodes*0.9)):
       G.add_node(len(G.nodes()))
       G.nodes[len(G.nodes())-1]['status'] = 5 # status 5 for born
def animate_infection(G):
   pos = nx.spring_layout(G)
   healthy = [node for node in G.nodes if G.nodes[node]['status'] == 0]
   infected = [node for node in G.nodes if G.nodes[node]['status'] == 1]
   recovered = [node for node in G.nodes if G.nodes[node]['status'] == 2]
   dead = [node for node in G.nodes if G.nodes[node]['status'] == 3]
   born = [node for node in G.nodes if G.nodes[node]['status'] == 4]

   nx.draw_networkx_nodes(G, pos, nodelist=healthy, node_color='g')
   nx.draw_networkx_nodes(G, pos, nodelist=infected, node_color='r')
   nx.draw_networkx_nodes(G, pos, nodelist=recovered, node_color='b')
   nx.draw_networkx_nodes(G, pos, nodelist=dead, node_color='black')
   nx.draw_networkx_nodes(G, pos, nodelist=born, node_color='yellow')
   nx.draw_networkx_edges(G, pos)
   # remove dead nodes
   dead_nodes = [node for node in G.nodes if G.nodes[node]['status'] == 3]
   G.remove_nodes_from(dead_nodes)

   spread_infection(G)
   cure_infected(G)

# animation start
for _ in range(10):
   animate_infection(G)
   plt.show()

