class Location:
    def __init__(self, height, neighbours):
        self.height = height
        self.neighbours = neighbours
    
    def isLow(self):
        lowest = True
        for h in self.neighbours:
            if h <= self.height:
                lowest = False
        return lowest

def basins():
    with open ("Day9\input.txt", "r") as f:
        floor = f.readlines()
    floor = list(map(lambda x: list(x.strip()), floor))
    floor = list(map(lambda x: [9] + x + [9], floor))
    padding = [[9] * len(floor[0])]
    floor = padding + floor + padding

    lowPoints = []
    for row in range(1, len(floor)-1):
        for col in range(1, len(floor[row])-1):
            height = int(floor[row][col])
            nHeight = int(floor[row-1][col])
            eHeight = int(floor[row][col+1])
            sHeight = int(floor[row+1][col])
            wHeight = int(floor[row][col-1])
            neighbours = [nHeight, eHeight, sHeight, wHeight]
            point = Location(height, neighbours)
            if point.isLow():
                lowPoints.append([point.height, row, col])

    sizes = []
    for point in lowPoints:
        q = [point]
        count = 0
        seen = []
        while q != []:
            n = q.pop(0)
            row, col = n[1], n[2]
            if n not in seen and n[0] != 9:
                count += 1
                q.append([int(floor[row-1][col]), row-1, col])
                q.append([int(floor[row][col+1]), row, col+1])
                q.append([int(floor[row+1][col]), row+1, col])
                q.append([int(floor[row][col-1]), row, col-1])
            seen.append(n)
        sizes.append(count)
    
    result = sorted(sizes)
    return result[-1]*result[-2]*result[-3]

print(basins()) #1019700