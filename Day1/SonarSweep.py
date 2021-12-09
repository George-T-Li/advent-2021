def depth_increases(fname):
    with open(fname, "r") as f:
        lines = f.readlines()
    prev = 9999
    count = 0

    for line in lines:
        curr = int(line)
        if curr > prev: count += 1
        prev = curr

    return count

print(depth_increases("Day1\input.txt")) #1676

def sliding_window(fname):
    with open(fname, "r") as f:
        lines = f.readlines()
    count = 0

    for i in range(len(lines[:-3])):
        curr = int(lines[i])
        comp = int(lines[i+3])
        if curr < comp: count += 1

    return count

print(sliding_window("Day1\input.txt")) #1706
    