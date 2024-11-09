import random

# Constants
BOARD_SIZE = 4


def welcome_message():
    """Prints the welcome message for the game."""
    print("Welcome to Battle Ship")
    print("There's a hidden battleship somewhere on this board.\n"
          "Enter your row and column guesses to sink it!")


def build_board(dims):
    """Creates a square board based on the given dimensions."""
    return [['O' for _ in range(dims)] for _ in range(dims)]


def print_board(board):
    """Prints the current state of the board."""
    for row in board:
        print(*row)


def build_ship(dims):
    """Creates and returns ship positional coordinates."""
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


def user_guess(dims):
    """Prompts the user for a guess and returns it as a tuple."""
    while True:
        try:
            row = int(input('Row: ')) - 1
            col = int(input('Col: ')) - 1
            if 0 <= row < dims and 0 <= col < dims:
                return (row, col)
            else:
                print(f"Please enter numbers between 1 and {dims}.")
        except ValueError:
            print("Please enter valid integers for row and column.")


def update_board(guess, board, ship, guesses):
    """Updates the board based on the user's guess."""
    if guess in guesses:
        print("Oops! You’ve already guessed there! Trying to trick the ocean, are we?")
        return board
    guesses.add(guess)
    if guess in ship:
        print("You hit my battleship!")
        board[guess[0]][guess[1]] = 'X'
        ship.remove(guess)
    else:
        print("LOL miss!")
    return board


def main():
    """Main function to run the Battleship game."""
    welcome_message()
    board = build_board(BOARD_SIZE)
    ship = build_ship(BOARD_SIZE)
    guesses = set()
    while ship:
        print_board(board)
        guess = user_guess(BOARD_SIZE)
        board = update_board(guess, board, ship, guesses)
    print("Congratulations! You've sunk the battleship!")


if __name__ == "__main__":
    main()