import networkx as nx

x = [y.split("-") for y in open(0).read().splitlines()]
g = nx.Graph()
g.add_edges_from(x)

c = list(nx.clique.find_cliques(g))

m = -1
v = None

for clique in c:
    if len(clique) > m:
        m = len(clique)
        v = clique

v.sort()

for n in v:
    print(n, end=",")
print()

# triangles = []
# for u, v in g.edges():
#     for w in g.neighbors(u):
#         if g.has_edge(w, v) and w != v:
#             triangle = tuple(sorted([u, v, w]))
#             if triangle not in triangles:
#                 triangles.append(triangle)

# filtered_triangles = []
# for t in triangles:
#     if any([n[0] == "t" for n in t]):
#         filtered_triangles.append(t)

# print(len(filtered_triangles))