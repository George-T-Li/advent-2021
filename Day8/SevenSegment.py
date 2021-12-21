"""
    # of segments: value1, value2, ...
    two: 1
    three: 7
    four: 4
    five: 2, 3, 5
    six: 0, 6, 9
    seven: 8
"""

"""
     aaaa
    b    c
    b    c
     dddd
    e    f
    e    f
     gggg
"""

def segments():
    with open("Day8\input.txt", "r") as f:
        patterns = f.readlines()

    count = 0
    for pattern in patterns:
        pattern = pattern.split("|")
        signals = pattern[0].split()
        output = pattern[1].split()
        for digit in output:
            if len(digit) in [2, 3, 4, 7]:
                count += 1
    
    return count

#print(segments()) #530

def parse_segments():
    with open("Day8\input.txt", "r") as f:
        patterns = f.readlines()

    count = 0
    for pattern in patterns:
        pattern = pattern.split("|")
        signals = pattern[0].split()
        output = pattern[1].split()
        value = decode(signals, output)
        print(value[0])
        count += value[1]
    
    return count

def decode(signals, output):
    twoSeg, threeSeg, fourSeg, sevenSeg = "", "", "", ""
    fiveSeg, sixSeg = [], []
    mapping = {}
    
    for signal in signals:
        if len(signal) == 2: twoSeg = signal
        elif len(signal) == 3: threeSeg = signal
        elif len(signal) == 4: fourSeg = signal
        elif len(signal) == 5: fiveSeg.append(signal)
        elif len(signal) == 6: sixSeg.append(signal)
        else: sevenSeg = signal
    
    #determine segments, a, c, f
    cORf = ""
    for char in threeSeg:
        if char not in twoSeg: mapping[char] = "a"
        else: cORf += char
    for digit in sixSeg:
        if cORf[0] not in digit:
            mapping[cORf[0]] = "c"
            mapping[cORf[1]] = "f"
            break
    else:
        mapping[cORf[0]] = "f"
        mapping[cORf[1]] = "c"

    #determine segment b and d
    bORd = ""
    for char in fourSeg:
        if char not in twoSeg: bORd += char
    for digit in sixSeg:
        if bORd[0] not in digit:
            mapping[bORd[0]] = "d"
            mapping[bORd[1]] = "b"
            break
    else:
        mapping[bORd[0]] = "b"
        mapping[bORd[1]] = "d"
    
    outValue = []
    for digit in output:
        if len(digit) == 2: outValue.append(1)
        elif len(digit) == 3: outValue.append(7)
        elif len(digit) == 4: outValue.append(4)
        elif len(digit) == 7: outValue.append(8)
        elif len(digit) == 5:
            missing = 0
            for char in digit:
                if char not in mapping: missing += 1
            if missing == 2: outValue.append(2)
            else:
                for char in digit:
                    if char in mapping:
                        if mapping[char] == "c":
                            outValue.append(3)
                            break
                else:
                    outValue.append(5)
        elif len(digit) == 6:
            missing = 0
            for char in digit:
                if char not in mapping: missing += 1
            if missing == 1: outValue.append(9)
            else:
                for char in digit:
                    if char in mapping:
                        if mapping[char] == "d":
                            outValue.append(6)
                            break
                else:
                    outValue.append(0)
    
    outValueNum = ""
    for digit in outValue:
        outValueNum += str(digit)
    outValueNum = int(outValueNum)
    
    return [outValue, outValueNum]

print(parse_segments()) #1051087