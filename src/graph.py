import osmnx as ox
import networkx as nx
class Graph:
    def __init__(self,graph_file="../san_miguel.graphml" ):
        self.graph = ox.load_graphml(graph_file) #../san_miguel.graphml
        self.edges = {}

    def add_node(self, value):
        self.nodes[value] = []

    def add_edge(self, from_node, to_node, distance):
        if from_node in self.nodes and to_node in self.nodes:
            self.edges[(from_node, to_node)] = distance
            self.nodes[from_node].append(to_node)
        else:
            raise ValueError("Both nodes must exist in the graph")

    def get_shortest_path(self, start_point, end_point):
        start_node = ox.get_nearest_node(self.graph, start_point)
        end_node = ox.get_nearest_node(self.graph, end_point)
        shortest_path = nx.shortest_path(self.graph, start_node, end_node, weight='length')
        return shortest_path
    