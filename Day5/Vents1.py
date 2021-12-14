def intersect():
    size = 1000
    with open("Day5\input.txt", "r") as f:
        lines = f.readlines()
        lines = cleanup(lines)
        lines = filter(is_hor_vert, lines)
        grid = [[0 for i in range(size)] for j in range(size)]

        for line in lines:
            x1 = min(line[0][0], line[1][0])
            x2 = max(line[0][0], line[1][0])
            y1 = min(line[0][1], line[1][1])
            y2 = max(line[0][1], line[1][1])
            xrange = range(x1, x2+1)
            yrange = range(y1, y2+1)
            for x in xrange:
                for y in yrange:
                    grid[x][y] += 1

        count = 0
        for x in range(size):
            for y in range(size):
                if grid[x][y] > 1: 
                    count += 1

        print(count)
                     
def cleanup(lines):
    clean_lines = []
    for line in lines:
        sline = line.split()
        p1 = sline[0].split(",")
        p2 = sline[2].split(",")
        p1 = (int(p1[0]), int(p1[1]))
        p2 = (int(p2[0]), int(p2[1]))
        clean_lines.append((p1, p2))
    return clean_lines

def is_hor_vert(line):
    x1 = line[0][0]
    x2 = line[1][0]
    y1 = line[0][1]
    y2 = line[1][1]
    if x1 == x2 or y1 == y2:
        return True
    else:
        return False

intersect() #4421