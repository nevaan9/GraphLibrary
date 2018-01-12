# Author: Nevaan Perera
# Purpose: implement an weighted undirected graph
# Citations:

from heapq import *
from graphs.graph import Graph


class WeightedGraph(Graph):
    # Weighted graph constructor.
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
        for (u, v, w) in edges:
            self.neighbors[u].add(v)
            self.neighbors[v].add(u)

        # Also store the edge weights
        self.weights = dict()
        for (u, v, w) in edges:
            self.weights[(u, v)] = w
            self.weights[(v, u)] = w

    # Dijkstra's algorithm: return a dictionary representing a search tree.
    # v = start vertex for the search
    def dijkstra(self, v):
        parents = {v: v}
        costs = {v: 0}
        frontier = [(0, v)]
        while len(frontier) > 0:
            (pcost, p) = heappop(frontier)
            if pcost == costs[p]:  # Ignore repeats
                for c in self.neighbors[p]:
                    d = pcost + self.weights[(p, c)]
                    if c not in costs or costs[c] > d:
                        parents[c] = p
                        costs[c] = d
                        heappush(frontier, (d, c))
        return parents

    # Return the total weight along this path in this graph.
    # path = deque of vertices
    def path_weight(self, path):
        total = 0
        v = None
        for u in path:
            if v is None:
                v = u
            else:
                total += self.weights[(v, u)]
                v = u
        return total

    # HOMEWORK 8 QUESTION
    def prims(self, v):
        parents = {v: v}
        costs = {v: 0}
        frontier = [(0, v)]
        finished = set()
        while len(frontier) > 0:
            (pcost, p) = heappop(frontier)
            finished.add(p)
            for c in self.neighbors[p]:
                if c not in finished:
                    w = self.weights[(p, c)]
                    if c not in costs or costs[c] > w:
                         parents[c] = p
                         costs[c] = w
                         heappush(frontier, (w, c))
        return parents


    # HOMEWORK 8 QUESTION
    def tree(self, parents):
        resultSet = set()
        edges = tuple(parents.items())

        for aTuple in edges:
            if aTuple[0] != aTuple[1]:
                resultSet.add(aTuple)

        return resultSet



def test():
    # Create an example graph
    vertices = {'A', 'B', 'C', 'D', 'E'}
    edges = {('A', 'B', 4), ('A', 'C', 2), ('B', 'C', 1), ('B', 'D', 3), ('C', 'E', 6), ('D', 'E', 1)}
    graph = WeightedGraph(vertices, edges)

    # What's the cheapest path from A to everywhere?
    parents = graph.dijkstra('A')
    for v in graph.vertices:
        path = Graph.path(v, parents)
        print(v, path, graph.path_weight(path))

# We are assuming that vertex1, vertex2 and vertex3 are all in the same component
# Argument 1: verticies in a graph
# Argument 2: edges in the graph
# Argument 3: Vertex you want to start at
# Argument 4: End vertex
# Argument 5: Vertext you want to pass by
def passThrough(verticies, edges, startVertex, endVertex, passByPoint):
    graph = WeightedGraph(verticies, edges)
    result = list()

    parents1 = graph.dijkstra(startVertex)
    path1 = Graph.path(passByPoint, parents1)

    parents2 = graph.dijkstra(passByPoint)
    path2 = Graph.path(endVertex, parents2)

    if path1 is None or path2 is None:
        return "The 3 verticies are not in the same compound, so it is not possible."

    for anItem in path1:
        result.append(anItem)

    for i in range(1, len(path2)):
        result.append(path2[i])

    return " -> ".join(result)


def notPassThrough(verticies, edges, startVertex, endVertex, notPassByPoint):
    edgesCopy = set()
    result = list()

    for aTuple in edges:
        if notPassByPoint not in aTuple:
            edgesCopy.add(aTuple)

    graph = WeightedGraph(verticies, edgesCopy)

    parents = graph.dijkstra(endVertex)
    path = Graph.path(startVertex, parents)

    for anItem in reversed(path):
        result.append(anItem)

    return " -> ".join(result)

def prims_run():
    # Create an example graph
    vertices = {'A', 'B', 'C', 'D', 'E', 'F', 'G'}
    edges = {('A', 'B', 7), ('B', 'C', 4), ('A', 'C', 9), ('D', 'A', 5), ('B', 'E', 5), ('B', 'F', 2), ('C', 'D', 7), ('C', 'F', 3), ('C', 'G', 4), ('D', 'G', 12), ('E', 'F', 2),('F','G',7)}
    graph = WeightedGraph(vertices, edges)

    # What's the cheapest path from A to everywhere?
    parents = graph.prims('A')

    print(parents)
    print(graph.tree(parents))



if __name__ == '__main__':
    vertices = {'A', 'B', 'C', 'D', 'E', 'F', 'G'}
    edges = {('A', 'B', 1), ('A', 'D', 2), ('A', 'E', 1), ('E', 'F', 1), ('E', 'C', 5), ('F', 'C', 1), ('B', 'C', 6)}
    print(passThrough(vertices, edges, 'A', 'D', 'B'))
    print("-"*40)

    vertices = {'A', 'B', 'C', 'D', 'E', 'F'}
    edges = {('A', 'B', 4), ('B', 'C', 3), ('A', 'D', 2), ('D', 'E', 5), ('B', 'E', 1), ('E', 'F', 2), ('C', 'F', 4)}
    print(notPassThrough(vertices, edges, 'A', 'B', 'C'))
    print()

    prims_run()

