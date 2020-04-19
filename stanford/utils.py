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
