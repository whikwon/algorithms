from graph import DiGraph, Node


def init_single_source(G, s):
    for v in G.node:
        v.d = float('inf')
        v.pi = None
    s.d = 0


def relax(u, v, w):
    """
    edge goes u -> v and takes w(weight)
    """
    if v.d > u.d + w:
        v.d = u.d + w
        v.pi = u


def bellman_ford(G, s):
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


def main():
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


if __name__ == "__main__":
    main()
