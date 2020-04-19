"""
- https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/
- https://stackoverflow.com/questions/19472530/representing-graphs-data-structure-in-python
"""

from collections import defaultdict
from queue import Queue


class Graph(object):

    def __init__(self):
        self.node = list()
        self.adj = defaultdict(dict)
        self.edge_attr = defaultdict(dict)

    def add_edge(self, u, v, **attr):
        """undirected graph"""
        assert isinstance(u, Vertex) and isinstance(v, Vertex)

        if u not in self.node:
            self.node.append(u)
        if v not in self.node:
            self.node.append(v)

        datadict = self.adj[u].get(v, dict())
        datadict.update(attr)
        self.adj[u][v] = datadict
        self.adj[v][u] = datadict


class DiGraph(Graph):

    def __init__(self):
        self.node = list()
        self.succ = self.adj = dict()
        self.pred = dict()
        self.edge_attr = dict()

    def add_edge(self, u, v, **attr):
        """directed graph"""
        assert isinstance(u, Vertex) and isinstance(v, Vertex)

        if u not in self.succ:
            self.node.append(u)
            self.succ[u] = dict()
            self.pred[u] = dict()
        if v not in self.succ:
            self.node.append(v)
            self.succ[v] = dict()
            self.pred[v] = dict()

        datadict = self.succ[u].get(v, dict())
        datadict.update(attr)
        self.succ[u][v] = datadict
        self.pred[v][u] = datadict


class Vertex(object):

    def __init__(self, name):
        self.name = name
        self.color = None
        self.d = -1
        self.pi = None

    def __repr__(self):
        return f"Vertex({self.name}, {self.color}, {self.d})"


def bfs(G, s):
    vertices = G.node

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
    print(u)
    for v in G.adj[u]:
        if v.color == "white":
            v.pi = u
            time = dfs_visit(G, v, time)
    u.color = "black"
    time += 1
    u.f = time
    return time


def dfs(G):
    vertices = G.node

    # node init
    for u in vertices:
        u.color = "white"
        u.pi = None

    time = 0
    for u in vertices:
        if u.color == "white":
            time = dfs_visit(G, u, time)


def main():
    G0 = DiGraph()
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
