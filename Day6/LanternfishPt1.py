def lanternfish(days):
    count = 0
    with open("Day6\input.txt", "r") as f:
        lfish = f.readline()
        lfish = lfish.split(",")
        tracker = []
        for fish in [1, 2, 3, 4, 5]:
            tracker.append(fish_count(int(fish), days))
        for fish in lfish:
            count += tracker[int(fish)-1]
    print(count)

def fish_count(n, days):
    l = [n]
    for d in range(days):
        new_l = []
        for age in l:
            if age == 0:
                age = 6
                new_l.append(age)
                new_l.append(8)
            else:
                age -= 1
                new_l.append(age)
        l = new_l
    return len(l)

#lanternfish(80) #373378
