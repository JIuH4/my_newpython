import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_node("A", data={"name": "node A"})
G.add_node("B", data={"name": "node B"})
G.add_node("C", data={"name": "node C"})
G.add_node("D", data={"name": "node D"})

G.add_edge("A", "B")
G.add_edge("A", "C")
G.add_edge("C", "D")
nx.draw_networkx(G)
plt.show()
print(nx.shortest_path(G,"B","D"))

print(G.nodes["A"]["data"]["name"])
