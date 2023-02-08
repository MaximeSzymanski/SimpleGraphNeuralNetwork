from graph import graph

def generate_random_graph(n):
    g = Graph()
    nodes = [chr(i + ord("A")) for i in range(n)]
    for node in nodes:
        features = random.randint(1, 100)
        g.add_node(node, features)
 
    for node1 in nodes:
        for node2 in nodes:
            if node1 == node2:
                continue
            if random.random() < 0.5:
                g.add_edge(node1, node2)
 
    return g
