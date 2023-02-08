from graph import Graph
from utils import generate_random_graph
import random

num_graphs = 10 # Number of random graphs to generate
num_nodes = 5 # Number of nodes in each graph

# A lambda function to generate a random graph

# A list comprehension to generate the list of random graphs
graph_list : list[Graph]= [generate_random_graph(num_nodes) for i in range(num_graphs)]

for graph in graph_list:
    graph.display_graph()
