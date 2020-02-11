"""
- https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/
- https://stackoverflow.com/questions/19472530/representing-graphs-data-structure-in-python
- https://github.com/networkx/networkx
"""

from queue import Queue


class Graph(object):

    node_list_factory = list
    adjlist_inner_dict_factory = dict
    adjlist_outer_dict_factory = dict
    edge_attr_dict_factory = dict

    def __init__(self):
        self.node = self.node_list_factory()
        self.adj = self.adjlist_outer_dict_factory()

    def add_edge(self, u, v, **attr):
        """undirected graph"""
        assert isinstance(u, Node) and isinstance(v, Node)

        if u not in self.node:
            self.node.append(u)
            self.adj[u] = self.adjlist_inner_dict_factory()
        if v not in self.node:
            self.node.append(v)
            self.adj[v] = self.adjlist_inner_dict_factory()

        datadict = self.adj[u].get(v, self.edge_attr_dict_factory())
        datadict.update(attr)
        self.adj[u][v] = datadict
        self.adj[v][u] = datadict


class DiGraph(Graph):
    """directed graph"""

    def __init__(self):
        self.node = self.node_list_factory()
        self.succ = self.adj = self.adjlist_outer_dict_factory()
        self.pred = self.adjlist_outer_dict_factory()
        self.edge_attr = self.edge_attr_dict_factory()

    def add_edge(self, u, v, **attr):
        assert isinstance(u, Node) and isinstance(v, Node)

        if u not in self.succ:
            self.node.append(u)
            self.succ[u] = self.adjlist_inner_dict_factory()
            self.pred[u] = self.adjlist_inner_dict_factory()
        if v not in self.succ:
            self.node.append(v)
            self.succ[v] = self.adjlist_inner_dict_factory()
            self.pred[v] = self.adjlist_inner_dict_factory()

        datadict = self.adj[u].get(v, self.edge_attr_dict_factory())
        datadict.update(attr)
        self.succ[u][v] = datadict
        self.pred[v][u] = datadict


class Node(object):

    def __init__(self, name):
        self.name = name
        self.color = None
        self.d = -1
        self.f = float('inf')
        self.pi = None

    def __repr__(self):
        return f"Node({self.name}, {self.color}, {self.d}, {self.f})"


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
    v = Node("v")
    r = Node("r")
    s = Node("s")
    w = Node("w")
    t = Node("t")
    x = Node("x")
    y = Node("y")
    u = Node("u")

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
    x = Node("x")
    u = Node("u")
    v = Node("v")
    y = Node("y")
    w = Node("w")
    z = Node("z")

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
