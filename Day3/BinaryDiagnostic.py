def power_consumption(fname):
    with open(fname, "r") as f:
        lines = f.readlines()
    rateArr = [[0,0] for i in range(12)]
    g = []
    e = []
    gamma = ""
    epsilon = ""

    for line in lines:
        for bit in range(len(line)-1):
            if line[bit] == "0": rateArr[bit][0] += 1
            else: rateArr[bit][1] += 1

    for i in range(len(rateArr)):
        if rateArr[i][0] > rateArr[i][1]:
            g.append("0")
            e.append("1")
        else:
            g.append("1")
            e.append("0")
    
    gamma = gamma.join(g)
    gamma = int(gamma, 2)
    epsilon = epsilon.join(e)
    epsilon = int(epsilon, 2)

    return gamma * epsilon

print(power_consumption("Day3\input.txt")) #3277364

def life_support(fname):
    oxygen = oxygen_generator(fname)
    co2 = co2_scrubber(fname)
    return oxygen * co2

def oxygen_generator(fname):
    with open(fname, "r") as f:
        lines = f.readlines()
    keep = []
    for line in lines:
        keep.append(line[:-1])

    count = 0
    while len(keep) != 1:
        rateArr = [[0,0] for i in range(12)]
        temp = []
        for num in keep:
            if num[count] == "0": rateArr[count][0] += 1
            else: rateArr[count][1] += 1
        if rateArr[count][0] > rateArr[count][1]: moreZeroes = True
        else: moreZeroes = False
        for num in keep:
            if num[count] == "0" and moreZeroes: temp.append(num)
            elif num[count] == "1" and not moreZeroes: temp.append(num)
        count+=1
        keep = temp
    
    oxygen = int(keep[0], 2)
    return oxygen

def co2_scrubber(fname):
    with open(fname, "r") as f:
        lines = f.readlines()
    keep = []
    for line in lines:
        keep.append(line[:-1])

    count = 0
    while len(keep) != 1:
        rateArr = [[0,0] for i in range(12)]
        temp = []
        for num in keep:
            if num[count] == "0": rateArr[count][0] += 1
            else: rateArr[count][1] += 1
        if rateArr[count][0] > rateArr[count][1]: moreZeroes = True
        else: moreZeroes = False
        for num in keep:
            if num[count] == "0" and not moreZeroes: temp.append(num)
            elif num[count] == "1" and moreZeroes: temp.append(num)
        count+=1
        keep = temp
    
    co2 = int(keep[0], 2)
    return co2

print(life_support("Day3\input.txt")) #5736383