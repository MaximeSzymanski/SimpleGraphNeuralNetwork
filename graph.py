import matplotlib.pyplot as plt
import networkx as nx
import random

class Graph:
    def __init__(self):
        """
        Initializes a new instance of the Graph class.
        
        Creates an empty dictionary called `graph` to store the nodes and their neighbors.
        """
        self.graph = {}
 
    def add_node(self, node, features = 0):
        """
        Adds a new node to the graph.
        
        :param node: The ID of the node to be added, represented by a letter.
        :type node: str
        :param features: The features of the node to be added.
        :type features: int
        
        Adds the node and its features to the `graph` dictionary if it does not already exist in the graph.
        """
        if node not in self.graph:
            self.graph[node] = {"features": features, "neighbors": []}
 
    def add_edge(self, node1, node2):
        """
        Adds a new edge between two nodes in the graph.
        
        :param node1: The first node to be connected.
        :type node1: str
        :param node2: The second node to be connected.
        :type node2: str
        
        Adds node2 to the list of neighbors for node1 and vice versa.
        """
        if node1 is not node2:
            self.graph[node1]["neighbors"].append(node2)
            self.graph[node2]["neighbors"].append(node1)
        else:
            self.graph[node2]["neighbors"].append(node1)

 
    def get_graph(self):
        """
        Returns the graph.
        
        :return: A dictionary that represents the graph, with each node as a key and its features and neighbors as the values.
        :rtype: dict
        """
        return self.graph
    
    def get_node_features(self, node):
        """
        Returns the features of a given node.
        
        :param node: The ID of the node to retrieve the features for.
        :type node: str
        :return: The features of the node if it exists in the graph, otherwise None.
        :rtype: int or None
        """
        if node in self.graph:
            return self.graph[node]["features"]
        else:
            return None
        
    def generate_node_degrees(self):
        """
        Generates the degree of each node and updates the `features` field for each node.
        
        The degree of a node is defined as the number of edges connected to it. This method updates the `features` field for each node to be its degree.
        """
        for node in self.graph:
            self.graph[node]["features"] = len(self.graph[node]["neighbors"])
 
    def display_graph(self):
        G = nx.Graph()
        for node in self.graph:
            G.add_node(node)
        for node in self.graph:
            for neighbor in self.graph[node]["neighbors"]:
                G.add_edge(node, neighbor)
        pos = nx.spring_layout(G)
        node_colors = ['red', 'blue', 'green', 'yellow', 'purple']
        nx.draw(G, pos, with_labels=True,  cmap=plt.cm.viridis, node_color=node_colors)
        plt.show()
