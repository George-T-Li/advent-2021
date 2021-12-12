from GiantSquid1 import Board

def bingo():
    with open("Day4\input.txt", "r") as f:
        lines = f.readlines()
        guesses = [int(n) for n in lines[0].split(",")]
        grids = lines[2:]
        grids = [row.split() for row in grids]
        boards = [Board([[0, 0, 0, 0, 0] for i in range(5)]) for i in range(100)]

        for j, board in enumerate(boards):
            for r in range(5):
                for c in range(5):
                    board.load_square(r, c, int(grids[r+(6*j)][c]))

        count = 0
        for guess in guesses:
            for board in boards:
                if not board.win_condition():
                    board.mark_square(guess)
                    if board.win_condition():
                        count += 1
                        if count == 100:
                            return board.get_score(guess)

bingo() #7686