# kruskal.py

from graph import Graph
from disjoint_set import DisjointSet

def kruskal(graph):
    edges = sorted(graph.get_edges(), key=lambda edge: edge.distance)
    disjoint_set = DisjointSet(len(graph.cities))
    mst = []

    city_to_index = {city: idx for idx, city in enumerate(graph.cities)}

    for edge in edges:
        city1_index = city_to_index[edge.city1]
        city2_index = city_to_index[edge.city2]

        if disjoint_set.union(city1_index, city2_index):
            mst.append(edge)

    return mst
