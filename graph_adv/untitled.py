import networkx as nx
import matplotlib.pyplot as plt


def load_from_file(fname):
    """
    Reads a  weighted graph from a file.
    :param fname: name of the file
    :return: None
    """
    G = nx.Graph()
    with open(fname) as f:
        for line in f:
            if line:
                a, b = line.split()
                G.add_edge(a, b, weight=5)
    return G


def show_path(graph, path):
    """
    Draws the graph with the path on it
    :param graph: the graph that is the base for the path, an nx.Graph
    :param path: the path that will be displayed, a list/tuple of labels
    :return: None
    """
    pos = nx.shell_layout(graph)
    nx.draw_networkx_nodes(graph, pos, node_size=500)
    nx.draw_networkx_edges(graph, pos, edgelist=graph.edges(), width=1)
    nx.draw_networkx_labels(graph, pos, font_size=20, font_family='serif')
    nx.draw_networkx_edges(graph, pos, edgelist=[(path[i], path[i+1]) for i
                                                 in range(len(path) - 1)], width=6)
    plt.axis('off')
    plt.show()


def get_spanning_tree_dfs(G, root):
    stack = [root]
    res = nx.Graph()
    G = nx.to_dict_of_dicts(G)
    used = {root}
    while stack:
        curr = stack.pop()
        for n in G[curr]:
            if n not in used:
                used.add(n)
                res.add_edge(curr, n, weight=G[curr][n]['weight'])
                stack.append(n)
    return res

T = load_from_file('input.txt')
t = get_spanning_tree_dfs(T, '0')
show_path(t, [])
