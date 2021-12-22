from statistics import median

def autocomplete():
    with open("Day10\input.txt") as f:
        lines = f.readlines()

    scores = []
    incomplete = []

    for line in lines:
        result = parse(line)
        if not result[0]:
            incomplete.append(line)

    for line in incomplete:
        score = 0
        completionString = complete(line)
        score = scoring(completionString)
        scores.append(score)

    return median(scores)

def parse(line):
    opened = []
    matching = {"(": ")", "[": "]", "{": "}", "<": ">"}
    for char in line:
        if char == "(": opened.append("(")
        elif char == "[": opened.append("[")
        elif char == "{": opened.append("{")
        elif char == "<": opened.append("<")

        if char in [")", "]", "}", ">"]:
            toClose = opened.pop()
            if char != matching[toClose]:
                return True, char
    else:
        return False, None

def complete(line):
    opened = []
    matching = {"(": ")", "[": "]", "{": "}", "<": ">"}
    closed = []

    for char in line:
        if char == "(": opened.append("(")
        elif char == "[": opened.append("[")
        elif char == "{": opened.append("{")
        elif char == "<": opened.append("<")

        if char in [")", "]", "}", ">"]:
            toClose = opened.pop()
    
    for char in list(reversed(opened)):
        closed.append(matching[char])

    return closed

def scoring(string):
    table = {")": 1, "]": 2, "}": 3, ">": 4}
    score = 0
    for char in string:
        score *= 5
        score += table[char]
    
    return score

print(autocomplete()) #1105996483
