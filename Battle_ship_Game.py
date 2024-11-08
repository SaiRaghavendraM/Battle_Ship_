import random


def welcome_message():
    print("Welcome to Battle Ship")
    print("There's a hidden battleship somewhere on this board.\n"
          'Enter your row and column guesses to sink it!')


# Create a square board based on dims value
def build_board(dims):
    return [['O' for _ in range(dims)] for _ in range(dims)]


def print_board(board):
    for row in board:
        print(*row)


# Create and return ship positional coordinates
def build_ship(dims):
    len_ship = random.randint(2, dims)
    orientation = random.choice(['horizontal', 'vertical'])
    if orientation == 'horizontal':
        row = random.randint(0, dims - 1)
        col_start = random.randint(0, dims - len_ship)
        coords = [(row, col) for col in range(col_start, col_start + len_ship)]
    else:
        col = random.randint(0, dims - 1)
        row_start = random.randint(0, dims - len_ship)
        coords = [(row, col) for row in range(row_start, row_start + len_ship)]
    return coords

def user_guess():
    while True:
        try:
            row = int(input('Row: ')) - 1
            col = int(input('Col: ')) - 1
            return (row, col)
        except ValueError:
            print("Please enter valid integers for row and column.")

def update_board(guess, board, ship, guesses):
    if guess in guesses:
        print('Oops! You’ve already guessed there! Trying to trick the ocean, are we?')
        return board
    guesses.add(guess)
    if guess in ship:
        print('You hit my battleship!')
        board[guess[0]][guess[1]] = 'X'
        ship.remove(guess)
    else:
        print('LOL miss!')
    return board

def main():
    welcome_message()
    dims = 4
    board = build_board(dims)
    ship = build_ship(dims)
    guesses = set()
    while ship:
        print_board(board)
        guess = user_guess()
        board = update_board(guess, board, ship, guesses)

main()