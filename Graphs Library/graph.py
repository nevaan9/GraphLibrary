# Author: Nevaan Perera
# Purpose: implement an unweighted undirected graph
# Citations:

from collections import deque


class Graph(object):
    # Graph constructor.
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
        for (u, v) in edges:
            self.neighbors[u].add(v)
            self.neighbors[v].add(u)

    # Depth-first search: mark all vertices reachable from v.
    # marks = set that will contain all the marked vertices
    def dfs(self, v, marks):
        marks.add(v)
        for u in self.neighbors[v]:
            if u not in marks:
                self.dfs(u, marks)

    # Breadth-first search: return a dictionary representing a search tree.
    # v = start vertex for the search
    def bfs(self, v):
        parents = {v: v}
        frontier = deque([v])
        while len(frontier) > 0:
            p = frontier.popleft()
            for c in self.neighbors[p]:
                if c not in parents:
                    parents[c] = p
                    frontier.append(c)
        return parents

    # Return a path starting from the root of a search tree.
    # v = vertex at the end of the path
    # parents = dictionary representing the search tree
    @staticmethod
    def path(v, parents):
        if v in parents:
            path = deque([v])
            while v != parents[v]:
                v = parents[v]
                path.appendleft(v)
            return path

    # Return a set of components in this graph.
    # Each component is a frozenset of vertices.
    def components(self):
        components = set()
        allMarks = set()
        for v in self.vertices:
            if v not in allMarks:
                marks = set()
                self.dfs(v, marks)
                allMarks |= marks
                components.add(frozenset(marks))
        return components


def test():
    # Create an example graph
    vertices = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    edges = {(1, 2), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (5, 9), (6, 7), (6, 8), (7, 8)}
    graph = Graph(vertices, edges)

    # What vertices are reachable from 1?
    marks = set()
    graph.dfs(1, marks)
    print(marks)

    # What's the shortest path from 1 to everywhere else?
    parents = graph.bfs(1)
    for v in graph.vertices:
        print(v, Graph.path(v, parents))

    # What are the components?
    print(graph.components())


if __name__ == '__main__':
    test()
