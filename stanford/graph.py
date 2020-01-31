"""
- https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/
- https://stackoverflow.com/questions/19472530/representing-graphs-data-structure-in-python
"""

from collections import defaultdict
from queue import Queue


class Graph(object):

    def __init__(self, directed=True):
        self.adj = defaultdict(set)
        self.directed = directed

    def add_edge(self, u, v):
        """undirected graph"""
        assert isinstance(u, Vertex) and isinstance(v, Vertex)
        self.adj[u].add(v)

        if not self.directed:
            self.adj[v].add(u)


class Vertex(object):

    def __init__(self, name):
        self.name = name
        self.color = None
        self.d = -1
        self.f = float('inf')
        self.pi = None

    def __repr__(self):
        return f"Vertex({self.name}, {self.color}, {self.d}, {self.f})"


def bfs(G, s):
    vertices = list(G.adj.keys())

    # node init
    for u in vertices:
        if u != s:
            u.color = "white"
            u.d = -1
            u.pi = None

    s.color = "gray"
    s.d = 0
    s.pi = None

    q = Queue()
    q.put(s)

    while not q.empty():
        u = q.get()
        for v in G.adj[u]:
            if v.color == "white":
                v.color = "gray"
                v.d = u.d + 1
                v.pi = u
                q.put(v)
        u.color = "black"
        print(u)
    return G


def dfs_visit(G, u, time):
    time += 1
    u.d = time
    u.color = "gray"

    for v in G.adj[u]:
        if v.color == "white":
            v.pi = u
            time = dfs_visit(G, v, time)

    time += 1
    u.f = time
    u.color = "black"
    print(u)
    return time


def dfs(G):
    vertices = list(G.adj.keys())

    # node init
    for u in vertices:
        u.color = "white"
        u.pi = None

    time = 0
    for u in vertices:
        if u.color == "white":
            time = dfs_visit(G, u, time)


def main():
    G0 = Graph(directed=False)
    v = Vertex("v")
    r = Vertex("r")
    s = Vertex("s")
    w = Vertex("w")
    t = Vertex("t")
    x = Vertex("x")
    y = Vertex("y")
    u = Vertex("u")

    G0.add_edge(v, r)
    G0.add_edge(r, s)
    G0.add_edge(s, w)
    G0.add_edge(w, t)
    G0.add_edge(w, x)
    G0.add_edge(t, x)
    G0.add_edge(t, u)
    G0.add_edge(x, u)
    G0.add_edge(x, y)
    G0.add_edge(u, y)

    G1 = Graph()
    x = Vertex("x")
    u = Vertex("u")
    v = Vertex("v")
    y = Vertex("y")
    w = Vertex("w")
    z = Vertex("z")

    G1.add_edge(u, x)
    G1.add_edge(u, v)
    G1.add_edge(x, v)
    G1.add_edge(v, y)
    G1.add_edge(y, x)
    G1.add_edge(w, y)
    G1.add_edge(w, z)
    G1.add_edge(z, z)

    print("========= BFS =========")
    bfs(G0, s)
    print("========= DFS =========")
    dfs(G1)


if __name__ == "__main__":
    main()
