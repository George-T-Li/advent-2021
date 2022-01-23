def main():
    with open("Day21\input.txt") as f:
        input = f.readlines()
    p1_pos = int(input[0][-2])
    p2_pos = int(input[1][-1])

    score = {1: 0, 2: 0}
    position = {1: p1_pos, 2: p2_pos}
    wins = {1: 0, 2: 0}

    universes = [[position, score, 1]]
    sums = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1} #value = # of occurrences

    player = 1
    while universes != []:
        new_unis = []
        for universe in universes:
            for sum, occ in sums.items():
                position = universe[0].copy()
                score = universe[1].copy()
                occurrence = universe[2]
                new_pos = (position[player] + sum) % 10
                if new_pos == 0:
                    new_pos = 10
                position[player] = new_pos
                score[player] += position[player]
                if score[player] >= 21:
                    wins[player] += occurrence*occ
                else:
                    new_unis.append([position, score, occurrence*occ])
        universes = new_unis.copy()
        player = 2 if player == 1 else 1 

    print(f'{wins = }')
    
if __name__ == "__main__":
    main()