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

        for guess in guesses:
            for board in boards:
                board.mark_square(guess)
                if board.win_condition():
                    board.show_board()
                    print(guess)
                    return board.get_score(guess)

class Board:
    def __init__(self, grid):
        self.grid = grid

    def show_board(self):
        print(self.grid)

    def load_square(self, r, c, n):
        """Puts n in square [r, c] in grid"""
        self.grid[r][c] = n

    def mark_square(self, n):
        """Marks square containing n and replace with 0"""
        for row in self.grid:
            if n in row:
                i = row.index(n)
                row[i] = -1
        return self.grid
    
    def win_condition(self):
        """Checks if bingo exists"""
        for row in self.grid:
            total = sum(row)
            if total == -5:
                return True
        for column in range(5):
            total = 0
            for row in self.grid:
                total += row[column]
            if total == -5:
                return True
        return False

    def get_score(self, guess):
        """Calculates the score of the board"""
        score = 0
        for row in self.grid:
            for i in row:
                if i != -1: score += i
        print(score * guess)

bingo() #34506