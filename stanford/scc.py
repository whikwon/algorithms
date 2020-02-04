"""
Strongly Connected Components,
Example from: Introduction to Algorithms, 3rd Edition. pp.616, Figure 22.9
"""

from collections import defaultdict
from copy import deepcopy

from graph import Graph, Vertex
from topological_sort import topological_sort


def dfs_visit(G, u, time, components):
    time += 1
    u.d = time
    u.color = "gray"
    components.append(u)

    for v in G.adj[u]:
        if v.color == "white":
            v.pi = u
            time, components = dfs_visit(G, v, time, components)

    time += 1
    u.f = time
    u.color = "black"
    return time, components


def _scc(G, vertices):
    # node init
    for u in vertices:
        u.color = "white"
        u.pi = None

    time = 0
    groups = []

    for u in vertices:
        if u.color == "white":
            components = []
            time, components = dfs_visit(G, u, time, components)
            groups.append(components)
    return groups


def scc(G):
    """Strongly Connected Components"""
    G_reversed = deepcopy(G)
    G_reversed.adj = defaultdict(set)

    for u in G.adj.keys():
        for v in G.adj[u]:
            G_reversed.adj[v].add(u)

    # topologically high to low
    sorted_vertices = topological_sort(G)[::-1]

    groups = _scc(G_reversed, sorted_vertices)
    return groups


def main():
    G = Graph()
    a = Vertex("a")
    b = Vertex("b")
    c = Vertex("c")
    d = Vertex("d")
    e = Vertex("e")
    f = Vertex("f")
    g = Vertex("g")
    h = Vertex("h")

    G.add_edge(a, b)
    G.add_edge(e, a)
    G.add_edge(b, e)
    G.add_edge(b, f)
    G.add_edge(b, c)
    G.add_edge(e, f)
    G.add_edge(f, g)
    G.add_edge(g, f)
    G.add_edge(c, g)
    G.add_edge(c, d)
    G.add_edge(d, c)
    G.add_edge(d, h)
    G.add_edge(g, h)
    G.add_edge(h, h)

    groups = scc(G)
    print(groups)


if __name__ == "__main__":
    main()
