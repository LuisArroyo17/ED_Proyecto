
from conectarDB import DB

# from models.arista import ModelArista

db= DB().connection()

# place_name = "San Juan de Lurigancho, Perú"
# G = ox.graph_from_place(place_name, network_type="drive")

# for node in G.nodes:
#   lat = G.nodes[node]["y"]
#   long = G.nodes[node]["x"]
#   ModelNodo().post_one_nodo(node, lat, long)

# # for node in G.nodes:
# #   # print(f"id: {node}, latitud: {G.nodes[node]['y']}, longitud: {G.nodes[node]['x']}")
# #   for neighbor in G.neighbors(node):
# #     distance = G.edges[node, neighbor, 0]["length"]
#     # print(f"id: {neighbor}, latitud: {G.nodes[neighbor]['y']}, longitud: {G.nodes[neighbor]['x']}")
#     #print(distance)
#     #ModelArista().post_one_arist(node, neighbor, distance)
