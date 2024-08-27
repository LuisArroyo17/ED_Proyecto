import osmnx as ox
import networkx as nx

# Especificar el nombre del distrito y país
place_name = "San Miguel, Lima, Peru"

# Descargar el grafo de la red vial de San Miguel
graph = ox.graph_from_place(place_name, network_type='drive')

# Mostrar información básica del grafo
print(f"Number of nodes: {graph.number_of_nodes()}")
print(f"Number of edges: {graph.number_of_edges()}")
print(f"Is directed: {graph.is_directed()}")
ox.save_graphml(graph, "san_miguel.graphml")