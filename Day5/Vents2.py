def intersect():
    size = 1000
    with open("Day5\input.txt", "r") as f:
        lines = f.readlines()
        lines = cleanup(lines)
        hv_lines = filter(is_hor_vert, lines)
        d_lines = filter(is_diag, lines)
        grid = [[0 for i in range(size)] for j in range(size)]

        for line in hv_lines:
            x1 = min(line[0][0], line[1][0])
            x2 = max(line[0][0], line[1][0])
            y1 = min(line[0][1], line[1][1])
            y2 = max(line[0][1], line[1][1])
            xrange = range(x1, x2+1)
            yrange = range(y1, y2+1)
            for x in xrange:
                for y in yrange:
                    grid[x][y] += 1

        for line in d_lines:
            x1 = line[0][0]
            x2 = line[1][0]
            y1 = line[0][1]
            y2 = line[1][1]
            if x1 < x2 and y1 < y2:
                for i in range(x2 - x1 + 1):
                    grid[x1+i][y1+i] += 1
            elif x1 < x2 and y1 > y2:
                for i in range(x2 - x1 + 1):
                    grid[x1+i][y1-i] += 1
            elif x1 > x2 and y1 < y2:
                for i in range(x1 - x2 + 1):
                    grid[x1-i][y1+i] += 1
            else:
                for i in range(x1 - x2 + 1):
                    grid[x1-i][y1-i] += 1

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

def is_diag(line):
    return not is_hor_vert(line)

intersect() #4421