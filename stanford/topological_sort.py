"""
Topological Sort
Example from: Introduction to Algorithms, 3rd Edition. pp.613, Figure 22.7
"""

from graph import Graph, Vertex


def dfs_visit(G, u, time, vertices_sorted):
    time += 1
    u.d = time
    u.color = "gray"

    for v in G.adj[u]:
        if v.color == "white":
            v.pi = u
            time, vertices_sorted = dfs_visit(G, v, time, vertices_sorted)

    time += 1
    u.f = time
    u.color = "black"
    vertices_sorted.append(u)
    return time, vertices_sorted


def topological_sort(G):
    """Topological sort for Directed Acyclic Graphs"""
    vertices = list(G.vertices)

    # node init
    for u in vertices:
        u.color = "white"
        u.pi = None

    time = 0
    vertices_sorted = []

    for u in vertices:
        if u.color == "white":
            time, vertices_sorted = dfs_visit(G, u, time, vertices_sorted)
    return vertices_sorted


def main():
    G = Graph(directed=True)
    undershorts = Vertex("undershorts")
    pants = Vertex("pants")
    belt = Vertex("belt")
    shirt = Vertex("shirt")
    tie = Vertex("tie")
    jacket = Vertex("jacket")
    socks = Vertex("socks")
    shoes = Vertex("shoes")
    watch = Vertex("watch")

    G.add_edge(shirt, belt)
    G.add_edge(shirt, tie)
    G.add_edge(tie, jacket)
    G.add_edge(belt, jacket)
    G.add_edge(pants, belt)
    G.add_edge(undershorts, shoes)
    G.add_edge(undershorts, pants)
    G.add_edge(pants, shoes)
    G.add_edge(socks, shoes)
    G.add_edge(watch, watch)

    vertices_sorted = topological_sort(G)
    # Can have more than 1 answers
    print(vertices_sorted)


if __name__ == "__main__":
    main()
