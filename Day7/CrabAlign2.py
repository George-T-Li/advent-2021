with open("Day7\input.txt", "r") as f:
    positions = f.readline()
    positions = positions.split(",")
    positions = list(map(int , positions))

def crab_align():
    minFuel = 999999999
    pos = 0
    maxPos = max(positions)

    for p in range(maxPos + 1):
        fuelUsed = 0
        for crab in positions:
            if fuelUsed < minFuel:
                fuelUsed += triangle(abs(crab - p))
            else:
                break
        else:
            if fuelUsed < minFuel:
                minFuel = fuelUsed
                pos = p
    
    return pos, minFuel

def triangle(n):
    return int(n*(n+1)/2)

print(crab_align()) #(478, 101079875.0)