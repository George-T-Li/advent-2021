from typing import DefaultDict

with open("Day12\input.txt") as f:
    input = f. readlines()
connections = []
for line in input:
    line = (line.strip()).split("-")
    enil = list(reversed(line))
    connections.append(tuple(line))
    connections.append(tuple(enil))
nodes = DefaultDict(list)
for key, value in connections:
    nodes[key].append(value)
paths = []

def pathfinding(path, seen):
    currNode = path[-1]
    if currNode == "end":
        paths.append(path)
    else:
        neighbours = nodes[currNode]
        for n in neighbours:
            if n.islower() and n not in seen:
                newpath = path + [n]
                newseen = seen + [n]
                pathfinding(newpath, newseen)
            elif n.isupper():
                newpath = path + [n]
                pathfinding(newpath, seen)

pathfinding(["start"], ["start"])
print(f"number of paths: {len(paths)}") #3421