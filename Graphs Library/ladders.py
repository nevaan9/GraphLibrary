# Author: Nevaan Perera
# Purpose: find word ladders
# Citations:

from graphs.graph import Graph

# Read in the words
words = open("words.txt", "r").read().split()

# Start some sets
vertices = set()
edges = set()

# Optimized algorithm

specialDict = dict()

for aWord in words:
    vertices.add(aWord)
    for i in range(len(aWord)):
        newWord = aWord[0:i] + "*" + aWord[i + 1:]
        if newWord not in specialDict:
            specialDict[newWord] = [aWord]
        else:
            for aConnection in specialDict[newWord]:
                edges.add((aWord, aConnection))
            specialDict[newWord].append(aWord) 


# Construct the graph
graph = Graph(vertices, edges)

# Find word ladders
while True:

    source = input("Source word: ")
    if source not in vertices:
        print("Unknown word:", source, "\n")
        continue

    target = input("Target word: ")
    if target not in vertices:
        print("Unknown word:", target, "\n")
        continue

    parents = graph.bfs(source)
    ladder = Graph.path(target, parents)
    print("Shortest ladder:", ladder, "\n")