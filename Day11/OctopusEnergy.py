def energy(n):
    with open ("Day11\input.txt", "r") as f:
        octopuses = f.readlines()
    octopuses = list(map(lambda x: list(x.strip()), octopuses))
    newoctopuses = []
    for row in octopuses:
        newrow = list(map(int, row))         
        newoctopuses.append(newrow)
    octopuses = newoctopuses
    octopuses = list(map(lambda x: [10] + x + [10], octopuses))
    padding = [[10] * len(octopuses[0])]
    octopuses = padding + octopuses + padding
    total = 0
    grid = []
    for row in range(1, len(octopuses)-1):
            for col in range(1, len(octopuses[row])-1):
                grid.append((row, col))

    for i in range(n):
        toflash = []
        flashed = []
        count = 0
        for row in range(1, len(octopuses)-1):
            for col in range(1, len(octopuses[row])-1):
                octopuses[row][col] += 1
                if octopuses[row][col] > 9:
                    toflash.append((row, col))

        while toflash != []:
            o = toflash.pop(0)
            r, c = o[0], o[1]
            neighbours = [(r-1, c), (r, c+1), (r+1, c), (r, c-1), (r-1, c+1), (r+1, c+1), (r+1, c-1), (r-1, c-1)]
            for n in neighbours:
                if n in grid:
                    octopuses[n[0]][n[1]] += 1
                    if octopuses[n[0]][n[1]] > 9 and n not in flashed and n not in toflash:
                        toflash.append((n[0], n[1]))
            flashed.append((o[0], o[1]))

        for o in flashed:
            octopuses[o[0]][o[1]] = 0
            count += 1
        if len(flashed) == 100:
            return(i+1)

        total += count
    return total

#print(energy(100)) 1661
print(energy(500)) #step 334