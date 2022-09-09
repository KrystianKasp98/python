import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


def prepare_graph(mapped_items, edges, positions):

    g = nx.DiGraph()
    nodes = np.arange(0, len(mapped_items)).tolist()

    g.add_nodes_from(nodes)

    g.add_edges_from(edges)

    nx.draw_networkx(g, pos=positions, labels=mapped_items, arrows=False, node_shape="s", node_color="white")

    plt.title("Organogram of a kingdom.")
    plt.savefig("Output/plain organogram using networkx.jpeg", dpi=300)
    plt.show()

