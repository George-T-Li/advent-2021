class Location:
    def __init__(self, height, neighbours):
        self.height = height
        self.neighbours = neighbours
    
    def isLow(self):
        compare = []
        lowest = True
        for h in self.neighbours:
            if h is not None:
                compare.append(h)
        for h in compare:
            if h <= self.height:
                lowest = False
        return lowest

def lowPoints():
    with open ("Day9\input.txt", "r") as f:
        floor = f.readlines()
        floor = list(map(lambda x: x.strip(), floor))

    points = []
    for row in range(len(floor)):
        for col in range(len(floor[row])):
            height = floor[row][col]
            try: 
                nHeight = floor[row-1][col]
                if row == 0: nHeight = None
            except: nHeight = None
            try: 
                eHeight = floor[row][col+1]
                if col == len(floor[row])-1: eHeight = None
            except: eHeight = None
            try:
                sHeight = floor[row+1][col]
                if row == len(floor)-1: sHeight = None
            except: sHeight = None
            try: 
                wHeight = floor[row][col-1]
                if col == 0: wHeight = None
            except: wHeight = None
            neighbours = [nHeight, eHeight, sHeight, wHeight]
            point = Location(height, neighbours)
            points.append(point)

    lowPoints = []
    total = 0
    for point in points:
        if point.isLow():
            lowPoints.append(point.height)
            riskLevel = int(point.height) + 1
            total += riskLevel
    
    return total

print(lowPoints())
