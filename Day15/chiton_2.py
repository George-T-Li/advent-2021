def main():
    with open("Day15\input.txt") as f:
        input = f.readlines()
    input = parse_input(input)

    grid_size = len(input)
    start, end = (0, 0), (grid_size - 1, grid_size - 1)
    vertices = [(x, y) for x in range(grid_size) for y in range(grid_size)]
    edges = get_edges(input, vertices)

    result = dijkstra(vertices, edges, start, end)

    print(result[0][end])
    
def parse_input(input):
    input = list(map(lambda x: x.strip(), (row for row in input)))
    input = list(map(lambda x: list(x), (row for row in input)))
    input = [list(map(int, (digit for digit in row))) for row in input]

    expanded_across = []
    #expand across
    for row in input:
        new_row = []
        for i in range(5):
            sub_row = row.copy()
            sub_row = [helper_add(x, i) for x in sub_row]
            new_row.extend(sub_row)
        expanded_across.append(new_row)

    expanded_input = []
    #expand down
    for i in range(5):
        for row in expanded_across:
            sub_row = row.copy()
            sub_row = [helper_add(x, i) for x in sub_row]
            expanded_input.append(sub_row)

    return expanded_input

def helper_add(x, i):
    x += i
    if x >= 10:
        return (x % 10) + 1
    else:
        return x

def get_edges(grid, V):
    edges = {}
    for v in V:
        neighbours = [(v[0], v[1]+1), (v[0], v[1]-1), (v[0]+1, v[1]), (v[0]-1, v[1])]
        for node in neighbours:
            if node in V:
                weight = get_risk(grid, node)
                edges[(v, node)] = weight
    return edges

def get_risk(grid, node):
    row = node[0]
    col = node[1]
    return grid[row][col]

def dijkstra(V, E, start, end):
    distance = {}
    predecessor = {}
    Q = set()

    for v in V:
        distance[v] = 9999
        predecessor[v] = None
        Q.add(v)
    distance[start] = 0

    while Q != {}:
        comp_distances = distance.copy()
        Q_distances = distance.copy()
        for key in comp_distances:
            if key not in Q:
                removed = Q_distances.pop(key)
        try:
            u = min(Q_distances, key=Q_distances.get)
        except:
            print("Q_distances is empty")
            print(distance)

        Q.remove(u)
        if u == end:
            s = []
            while u != None:
                s.append(u)
                u = predecessor[u]
            return s
            
        neighbours = [(u[0], u[1]+1), (u[0], u[1]-1), (u[0]+1, u[1]), (u[0]-1, u[1])]
        for node in neighbours:
            if node in V and node in Q:
                alt = distance[u] + E[(u, node)]
                if alt < distance[node]:
                    distance[node] = alt
                    predecessor[node] = u

    return distance, predecessor


if __name__ == "__main__":
    main()