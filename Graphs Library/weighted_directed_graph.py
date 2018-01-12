# Author: Lisa Torrey
# Purpose: implement a weighted directed graph
# Citations:

from graphs.directed_graphs import DirectedGraph
from graphs.weighted_graph import WeightedGraph

class DirectedWeightedGraph(DirectedGraph, WeightedGraph):

    # Directed weighted graph constructor.
    # vertices = set of vertex labels
    # edges = set of tuples of adjacent vertices with weights
    def __init__(self, vertices, edges):

        # Save the original sets
        self.vertices = vertices
        self.edges = edges

        # Also construct neighbor sets
        self.neighbors = dict()
        for v in vertices:
            self.neighbors[v] = set()
        for (u,v,w) in edges:
            self.neighbors[u].add(v)

        # Also store the edge weights
        self.weights = dict()
        for (u,v,w) in edges:
            self.weights[(u,v)] = w

def test():

    # Create an example graph
    vertices = {1, 2, 3, 4, 5, 6}
    edges = {(1,2,1), (2,3,1), (2,4,10), (3,5,1), (5,4,1), (5,6,1)}
    graph = DirectedWeightedGraph(vertices, edges)

    # Check Dijkstra's algorithm
    print(graph.dijkstra(2))

    # Check topological sort
    print(graph.topsort())

if __name__ == '__main__':
    test()