def parse_rules(list, pairs_count):
    rules = {}
    for rule in list:
        rules[rule[:2]] = rule[-2:].strip()
        pairs_count[rule[:2]] = 0
    return rules

def element_pairs(polymer):
    length = len(polymer)
    pairs = []
    for i in range(length-1):
        pairs.append(polymer[i] + polymer[i+1])
    return pairs

def insert(pairs_count, occurrences, rules):
    new_pairs_count = pairs_count.copy()
    for pair in pairs_count:
        count = pairs_count[pair]
        new_pairs_count[pair] -= count
        occurrences[rules[pair]] += count
        new_pair_1 = pair[0] + rules[pair]
        new_pair_2 = rules[pair] + pair[1]
        new_pairs_count[new_pair_1] += count
        new_pairs_count[new_pair_2] += count
    return new_pairs_count, occurrences

def main():
    with open("Day14\input.txt") as f:
        input = f.readlines()

    alpha = [chr(i) for i in range(65, 91)]
    pairs_count = {}
    occurrences = {char: 0 for char in alpha}

    polymer = input[0].strip()
    rules = parse_rules(input[2:], pairs_count)
    pairs = element_pairs(polymer)

    for pair in pairs:
        pairs_count[pair] = 1
    for element in polymer:
        occurrences[element] += 1
    
    for i in range(40):
        pairs_count, occurrences = insert(pairs_count, occurrences, rules)
    
    result = []
    for char in occurrences:
        if occurrences[char] != 0:
            print(f'{char}: {occurrences[char]}')
            result.append(occurrences[char])
    result.sort()
    print(f'difference: {result[-1] - result[0]}')
    
if __name__ == "__main__":
    main()