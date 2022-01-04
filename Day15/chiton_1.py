def main():
    with open("Day15\inputTest.txt") as f:
        input = f.readlines()
    input = parse_input(input)
    size = len(input)
    start, end = (0, 0), (size-1, size-1)
    accepted_values = [(x, y) for x in range(size) for y in range(size)]
    shortest_path(input, start, end, [start], accepted_values)
    print(memo[(start, end)])

def parse_input(input):
    input = list(map(lambda x: x.strip(), (row for row in input)))
    input = list(map(lambda x: list(x), (row for row in input)))
    input = [list(map(int, (digit for digit in row))) for row in input]
    return input

def shortest_path(grid, start, end, seen, accepted):
    if start == end:
        return 0
    elif (start, end) in memo:
        return memo[(start, end)]
    else:
        end_x, end_y = end[0], end[1]
        end_neighbours = [(end_x, end_y+1), (end_x, end_y-1), (end_x+1, end_y), (end_x-1, end_y)]
        paths = []
        print(end_neighbours)
        for node in end_neighbours:
            if node in accepted and node not in seen:
                new_seen = seen.copy()
                new_seen.append(node)
                test = shortest_path(grid, start, node, new_seen, accepted)
                print(f'{test = }')
                path = shortest_path(grid, start, node, new_seen, accepted) + grid[node[0]][node[1]]
                paths.append(path)
        memo[(start, node)] = min(paths, default = 0)

if __name__ == "__main__":
    memo = {}
    main()