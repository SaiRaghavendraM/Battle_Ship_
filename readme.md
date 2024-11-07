
# Battleship Game

Welcome to **Battleship**! This is a classic command-line game where the player tries to locate and sink a hidden battleship by making guesses. This project demonstrates foundational Python programming skills, including functions, loops, and handling user input.

## How to Play

In this game, the player is presented with a square board filled with `"O"` symbols. The computer hides a battleship on this board, which the player needs to find by guessing its location.

1. Enter the row and column number for your guess.
2. If you hit a part of the ship, the board will display an `"X"` at that position.
3. Continue guessing until you've sunk the entire ship!

The game will let you know if you've hit or missed.

## Features

- **Random Ship Placement**: The game randomly generates a ship, which can be horizontal or vertical.
- **Guess Validation**: The game prevents duplicate guesses and handles invalid inputs.
- **Interactive Board Updates**: Each guess updates the board visually to show hits and misses.

## Code Structure

- `welcome_message()`: Displays the game's welcome message and brief instructions.
- `build_board(dims)`: Creates a `dims x dims` board, represented as a list of lists.
- `print_board(board)`: Prints the current state of the game board.
- `build_ship(dims)`: Randomly generates a ship's position and orientation.
- `user_guess()`: Collects the player's row and column guesses and handles input errors.
- `update_board(guess, board, ship, guesses)`: Updates the board based on the player’s guess and indicates hits or misses.
- `main()`: The main game loop that calls functions to initialize the game, take guesses, and update the board.

## Getting Started

### Prerequisites
- Python 3.6 or higher.

### Running the Game
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/battleship-game.git
   ```
2. Navigate to the project directory:
   ```bash
   cd battleship-game
   ```
3. Run the game:
   ```bash
   python battleship_game.py
   ```

## Example Gameplay

```
Welcome to Battle Ship
There is a battleship hidden in this board.
Enter your row and column guesses to sink it!

O O O O
O O O O
O O O O
O O O O

Row: 2
Col: 3
LOL miss!

O O O O
O O O O
O O O O
O O O O

Row: 1
Col: 1
You hit my battleship!

O X O O
O O O O
O O O O
O O O O
```

## License

This project is licensed under the MIT License.