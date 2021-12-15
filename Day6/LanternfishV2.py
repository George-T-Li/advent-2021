with open("Day6\input.txt", "r") as f:
    lfish = f.readline()
    lfish = lfish.split(",")
    lfish = list(map(int , lfish))

def lanternfish(days):
    tracker = []
    for i in range(9):
        tracker.append(lfish.count(i))

    start = 0
    while start != days:
        new = []
        for i in range(8):
            if i != 6:
                new.append(tracker[i+1])
            else:
                new.append(tracker[0] + tracker[7])
        new.append(tracker[0])
        tracker = new
        start += 1

    return tracker, sum(tracker)

print(lanternfish(80))
print(lanternfish(256)) #1682576647495