def main():
    with open("Day15\input.txt") as f:
        input = f.readlines()
    input = parse_input(input)

    grid_size = len(input)
    start, end = (0, 0), (grid_size - 1, grid_size - 1)
    vertices = [(x, y) for x in range(grid_size) for y in range(grid_size)]
    edges = get_edges(input, vertices)

    result = bellman_ford(vertices, edges, start)

    print(result[0][end])
    
def parse_input(input):
    input = list(map(lambda x: x.strip(), (row for row in input)))
    input = list(map(lambda x: list(x), (row for row in input)))
    input = [list(map(int, (digit for digit in row))) for row in input]
    return input

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

def bellman_ford(vertices, edges, source):
    distance = {}
    predecessor = {}

    for v in vertices:
        distance[v] = 9999
        predecessor[v] = None

    distance[source] = 0

    for i in range(len(vertices)-1):
        for e in edges:
            u, v = e[0], e[1]
            w = edges[e]
            if distance[u] + w < distance[v]:
                distance[v] = distance[u] + w
                predecessor[v] = u

    return distance, predecessor

if __name__ == "__main__":
    main()