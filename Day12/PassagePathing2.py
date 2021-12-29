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
small = []
for key in dict(connections):
    if key.islower(): small.append(key)
paths = []

def pathfinding(path, seen, twice):
    currNode = path[-1]
    if currNode == "end":
        paths.append(str(path))
    else:
        neighbours = nodes[currNode]
        for n in neighbours:
            if n.islower() and n not in seen:
                newpath = path + [n]
                newseen = seen.copy()
                newseen[n] = 1
                pathfinding(newpath, newseen, twice)
            elif n.islower() and n == twice and seen[n] < 2:
                newpath = path + [n]
                newseen = seen.copy()
                newseen[n] = 2
                pathfinding(newpath, newseen, twice)
            elif n.isupper():
                newpath = path + [n]
                pathfinding(newpath, seen, twice)

for cave in small:
    if cave != "start" and cave != "end":
        pathfinding(["start"], {"start": 1}, cave)
nodupes = list(set(paths))
print(f"number of paths: {len(nodupes)}")