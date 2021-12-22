def corrupted():
    with open("Day10\input.txt") as f:
        lines = f.readlines()

    score = {")": 3, "]": 57, "}": 1197, ">": 25137}
    total = 0
    errors = []
    for line in lines:
        result = parse(line)
        if result[0]:
            total += score[result[1]]
            errors.append(result[1])
    return total, errors

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

print(corrupted()) #215229
