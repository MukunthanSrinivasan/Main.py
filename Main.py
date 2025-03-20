# main.py

from graph import Graph
from kruskal import kruskal

def main():
    cities = ["CityA", "CityB", "CityC", "CityD"]
    graph = Graph(cities)

    graph.add_edge("CityA", "CityB", 10)
    graph.add_edge("CityA", "CityC", 15)
    graph.add_edge("CityA", "CityD", 5)
    graph.add_edge("CityB", "CityD", 8)
    graph.add_edge("CityC", "CityD", 12)

    mst = kruskal(graph)

    print("Minimum Spanning Tree (MST):")
    for edge in mst:
        print(f"From {edge.city1} to {edge.city2}, Distance: {edge.distance}")

if __name__ == "__main__":
    main()
