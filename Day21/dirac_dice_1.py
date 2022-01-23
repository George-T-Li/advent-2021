def main():
    with open("Day21\input.txt") as f:
        input = f.readlines()
    p1_pos = int(input[0][-2])
    p2_pos = int(input[1][-1])
    scores = {1: 0, 2: 0}
    positions = {1: p1_pos, 2: p2_pos}

    d_die = [x for x in range(1, 101)]
    index = 0
    rolls = 0
    
    player = 1
    while scores[1] < 1000 and scores[2] < 1000:
        sum = 0
        for i in range(3):                          #roll dice
            sum += d_die[index]
            rolls += 1
            index = (index + 1) % 100
        new_pos = (positions[player] + sum) % 10
        if new_pos == 0:
            new_pos = 10
        positions[player] = new_pos                 #move player
        scores[player] += positions[player]         #add score
        player = 2 if player == 1 else 1            #switch player
    
    if scores[1] > scores[2]:
        print("P1 wins!")
        loser_score = scores[2]
    else:
        print("P2 wins!")
        loser_score = scores[1]

    print(f'{loser_score = }; {rolls = }; product = {loser_score*rolls}')

if __name__ == "__main__":
    main()