def fold(dots, direction, line):
    if direction == "left":
        dots = swap(dots)
    size = line * 2 + 1
    folded_dots = []
    for dot in dots:
        if dot[1] < line:            #dot is above fold
            folded_dots.append(dot)
        else:                        #dot is below fold
            dist_to_fold = dot[1] - line
            folded_dots.append((dot[0], line - dist_to_fold))
    if direction == "left":
        folded_dots = swap(folded_dots)
    return set(folded_dots)

def swap(dots):
    swapped = []
    for dot in dots:
        swapped.append((dot[1], dot[0]))
    return swapped

def main():
    with open("Day13\input.txt") as f:
        input = f. readlines()
    list_of_dots = input[:-13]
    instructions = input[-12:]
    dots = list(map(lambda x: tuple(map(int, (x.split(",")))), list_of_dots))

    dots = fold(dots, "left", 655)

    count = len(dots)
    print(f'{count = }')

if __name__ == "__main__":
    main()