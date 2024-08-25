class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = {}

    def add_node(self, value):
        self.nodes[value] = []

    def add_edge(self, from_node, to_node, distance):
        if from_node in self.nodes and to_node in self.nodes:
            self.edges[(from_node, to_node)] = distance
            self.nodes[from_node].append(to_node)
        else:
            raise ValueError("Both nodes must exist in the graph")

    def get_shortest_path(self, start_node, end_node):
        # Implementación de algoritmo para encontrar el camino más corto
        pass
