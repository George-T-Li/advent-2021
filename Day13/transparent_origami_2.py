def transpose(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    t_rows = ["" for i in range(num_rows)]
    t_matrix = [t_rows.copy() for j in range(num_cols)]
    for row, row_val in enumerate(matrix):
        for col, value in enumerate(row_val):
            t_matrix[col][row] = value
    return t_matrix
    
def fold(matrix, direction, line):
    if direction == "left":
        matrix = transpose(matrix)
    folded_matrix = matrix[:line].copy()
    remaining_rows = matrix[line+1:].copy()
    flipped_remaining_rows = reversed(remaining_rows)
    for row, row_val in enumerate(flipped_remaining_rows):
        for col, value in enumerate(row_val):
            if value == "#": folded_matrix[row][col] = "#"
    if direction == "left":
        folded_matrix = transpose(folded_matrix)
    return folded_matrix

def parse_instructions(list):
    parsed = []
    for instruction in list:
        line = int(instruction.strip("fold angxy="))
        if "x" in instruction:
            parsed.append(("left", line))
        else:
            parsed.append(("up", line))
    return parsed

def show(grid):
    for row in grid:
        print(row)

def main():
    with open("Day13\input.txt") as f:
        input = f. readlines()
    list_of_dots = input[:-13]
    instructions = parse_instructions(input[-12:])

    dots = list(map(lambda x: tuple(map(int, (x.split(",")))), list_of_dots))
    max_x, max_y = 1311, 895
    grid_rows = ["." for i in range(max_x)]
    grid = [grid_rows.copy() for j in range(max_y)]
    for dot in dots:
        grid[dot[1]][dot[0]] = "#"

    for step in instructions:
        grid = fold(grid, step[0], step[1])

    show(grid)

if __name__ == "__main__":
    main()