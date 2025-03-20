# graph.py

class Edge:
    def __init__(self, city1, city2, distance):
        self.city1 = city1
        self.city2 = city2
        self.distance = distance

    def __repr__(self):
        return f"({self.city1}, {self.city2}, {self.distance})"


class Graph:
    def __init__(self, cities):
        self.cities = cities
        self.edges = []

    def add_edge(self, city1, city2, distance):
        self.edges.append(Edge(city1, city2, distance))

    def get_edges(self):
        return self.edges
