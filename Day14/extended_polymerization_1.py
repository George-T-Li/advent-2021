def parse_rules(list):
    rules = {}
    for rule in list:
        rules[rule[:2]] = rule[-2:].strip()
    return rules

def element_pairs(polymer):
    length = len(polymer)
    pairs = []
    for i in range(length-1):
        pairs.append(polymer[i] + polymer[i+1])
    return pairs

def insert(polymer, rules):
    new_polymer = ""
    pairs = element_pairs(polymer)
    for pair in pairs:
        new_polymer += pair[0]
        if pair in rules:
            new_polymer += rules[pair]
        else:
            new_polymer += pair[1]
    new_polymer += polymer[-1]
    return new_polymer

def count_frequencies(polymer):
    occurrences = {}
    for element in polymer:
        if element in occurrences:
            occurrences[element] += 1
        else:
            occurrences[element] = 1
    return occurrences

def main():
    with open("Day14\input.txt") as f:
        input = f.readlines()
    polymer = input[0].strip()
    rules = parse_rules(input[2:])
    for i in range(10):
        polymer = insert(polymer, rules)
    occurrences = count_frequencies(polymer)
    print(occurrences)
    
if __name__ == "__main__":
    main()
    # O: 3800, V: 541