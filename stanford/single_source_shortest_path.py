"""
Single-Source Shortest Paths,
Example from: Introduction to Algorithms, 3rd Edition. pp.664-704
"""

from heapq import heappop, heappush
from itertools import count

from graph import DiGraph, Node
from topological_sort import topological_sort
from utils import init_single_source, relax


def bellman_ford(G, s):
    """no negative cycle"""
    init_single_source(G, s)

    # for every node in G
    for u in G.node[:-1]:
        # for every edge in G
        for u, vs in G.adj.items():
            for v in vs:
                w = G.adj[u][v]['w']
                relax(u, v, w)

    for u in G.node:
        for v in G.adj[u]:
            w = G.adj[u][v]['w']
            if v.d > u.d + w:  # when w is negative
                print("Error", u, v, w)
                return False
    return True


def dag_shortest_path(G, s):
    """no cycle"""
    vertices_sorted = topological_sort(G)
    init_single_source(G, s)

    for u in vertices_sorted:
        for v in G.adj[u]:
            relax(u, v, G.adj[u][v]['w'])


def dijkstra(G, s):
    """no negative edge"""
    init_single_source(G, s)

    S = {}
    Q = []  # min-priority queue
    c = count()

    pop = heappop
    push = heappush

    push(Q, (s.d, next(c), s))

    idx = 0
    while Q:
        dist, _, u = pop(Q)
        idx += 1
        if u in S:
            continue
        # shortest path for 'u' are calculated over before checking adj
        S[u] = dist
        for v in G.adj[u]:
            w = G.adj[u][v].get('w', 1)
            relax(u, v, w)
            push(Q, (v.d, next(c), v))
    return S


def test_bellman_ford():
    G = DiGraph()
    s = Node("s")
    t = Node("t")
    y = Node("y")
    x = Node("x")
    z = Node("z")

    G.add_edge(s, t, w=6)
    G.add_edge(s, y, w=7)
    G.add_edge(t, y, w=8)
    G.add_edge(t, x, w=5)
    G.add_edge(t, z, w=-4)
    G.add_edge(x, t, w=-2)
    G.add_edge(y, x, w=-3)
    G.add_edge(y, z, w=9)
    G.add_edge(z, x, w=7)
    G.add_edge(z, s, w=2)

    assert bellman_ford(G, s)


def test_dag_shortest_path():
    G = DiGraph()
    r = Node("r")
    s = Node("s")
    t = Node("t")
    x = Node("x")
    y = Node("y")
    z = Node("z")

    G.add_edge(r, s, w=5)
    G.add_edge(r, t, w=3)
    G.add_edge(s, x, w=6)
    G.add_edge(s, t, w=2)
    G.add_edge(t, x, w=7)
    G.add_edge(t, y, w=4)
    G.add_edge(t, z, w=2)
    G.add_edge(x, y, w=-1)
    G.add_edge(x, z, w=1)
    G.add_edge(y, z, w=-2)

    dag_shortest_path(G, s)

    assert [u.d for u in G.node] == [float('inf'), 0, 2, 6, 5, 3]


def test_dijkstra():
    G = DiGraph()
    s = Node("s")
    t = Node("t")
    y = Node("y")
    x = Node("x")
    z = Node("z")

    G.add_edge(s, t, w=10)
    G.add_edge(s, y, w=5)
    G.add_edge(t, y, w=2)
    G.add_edge(y, t, w=3)
    G.add_edge(t, x, w=1)
    G.add_edge(y, x, w=9)
    G.add_edge(y, z, w=2)
    G.add_edge(z, s, w=7)
    G.add_edge(z, x, w=6)
    G.add_edge(x, z, w=4)

    dijkstra(G, s)

    assert [u.d for u in G.node] == [0, 8, 5, 9, 7]


if __name__ == "__main__":
    test_bellman_ford()
    test_dag_shortest_path()
    test_dijkstra()
