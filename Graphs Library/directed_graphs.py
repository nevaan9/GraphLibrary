# Author: Nevaan Perera
# Purpose: implement an unweighted directed graph
# Citations:

from collections import deque
from graphs.graph import Graph

class DirectedGraph(Graph):

    # Directed graph constructor.
    # vertices = set of vertex labels
    # edges = set of tuples of adjacent vertices
    def __init__(self, vertices, edges):

        # Save the original sets
        self.vertices = vertices
        self.edges = edges

        # Also construct neighbor sets
        self.neighbors = dict()
        for v in vertices:
            self.neighbors[v] = set()
        for edge in edges:
            (u, v) = (edge[0], edge[1])
            self.neighbors[u].add(v)

    # Return a reversed copy of this graph.
    def reverse(self):
        vertices = set()
        edges = set()
        for v in self.vertices:
            vertices.add(v)
            for u in self.neighbors[v]:
                edges.add((u,v))
        return DirectedGraph(vertices, edges)

    # Override DFS: mark all vertices reachable from v that are not already marked.
    # Also make a topological ordering of those vertices.
    # newMarks = set that will contain all the newly marked vertices
    # allMarks = set that contains vertices that are already marked (optional)
    # order = deque where the topological order will be placed (optional)
    def dfs(self, v, newMarks, allMarks=None, order=None):

        # In case of default arguments
        if allMarks is None:
            allMarks = set()
        if order is None:
            order = deque()

        # Mark everything reachable from v
        newMarks.add(v)
        allMarks.add(v)
        for u in self.neighbors[v]:
            if u not in allMarks:
                self.dfs(u, newMarks, allMarks, order)

        # Put v on the front of the order so far
        order.appendleft(v)

    # Override components: return a set of strongly connected components in this graph.
    # Each component is a frozenset of vertices.
    def components(self):
        components = set()
        allMarks = set()
        for v in self.reverse().topsort():
            if v not in allMarks:
                marks = set()
                self.dfs(v, marks, allMarks)
                allMarks |= marks
                components.add(frozenset(marks))
        return components

    # Return a list of the vertices in topological order.
    # Will not report problems if there are cycles!
    def topsort(self):
        order = deque()
        marks = set()
        for v in self.vertices:
            if v not in marks:
                self.dfs(v, set(), marks, order)
        return order

def test():

    # Create an example graph
    vertices = {1, 2, 3, 4, 5, 6}
    edges = {(1,2),(2,3),(3,5),(5,4),(5,6)}
    graph = DirectedGraph(vertices, edges)
    graphR = graph.reverse()


    # Do a topological sort
    print(graph.topsort())

    # Add 4->2 edge to the graph
    graph.neighbors[4].add(2)

    # Look at the components
    print(graph.components())

if __name__ == '__main__':
    test()
