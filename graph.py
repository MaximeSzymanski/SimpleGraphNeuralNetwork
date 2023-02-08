class graph:
    def __init__(self):
        self.graph = {}
 
    def add_node(self, node, features):
        if node not in self.graph:
            self.graph[node] = {"features": features, "neighbors": []}
 
    def add_edge(self, node1, node2):
        self.graph[node1]["neighbors"].append(node2)
        self.graph[node2]["neighbors"].append(node1)
 
    def get_graph(self):
        return self.graph