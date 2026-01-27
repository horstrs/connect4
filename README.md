How to run (for now):
uv run python -m src.main

player turn overview:

# Input (View): The View captures the raw input (e.g., the string "3") and passes it directly to the Controller.
# Sanitization & Validation (Controller): The Controller checks if the input is an integer. It then asks the Model if that column is playable.
** Why? The View shouldn't know the rules of Connect 4 (like how many columns exist). If you change the board size in the Model, you shouldn't have to update the View.

# Update (Model): The Controller tells the Model to drop a piece. The Model updates its internal state and returns the result (e.g., the new row index or a "Success" status).

# Win/Tie Check (Model): The Controller asks the Model if the last move triggered a win or a draw.

# Render (View): The Controller sends the updated board data to the View to be printed.

Note: The View never asks the Model for data; the Controller acts as the middleman.

Player class:
Contains the player id, player name and the move strategy.
This class has a get_move(board) method, that should use the move_strategy instance to decide the next move. 
For now, we'll only have a HumanStrategy implementation for move_strategy, that will return a Signal (just a constant) informing the controller that an user input is required. 
Each AI strategy we implement will be a different implementation of this strategy and the calculate_move.

Board class:

The board should contain the number of rows and columns and a living board state, that's initialized in the constructor with 0.

The board_state would be just a list of lists, where the outter list represents the columns and the inner list represents the lines. And each cell would contain either 0 for empty cells, or 1 or 2 representing player 1 and player 2, respectively.


The methods needed for the board class are:

* Is_column_playable -> Receives a column indexes and if the index exists and is not yet full return True. Otherwise, return false

* Add piece -> Receives a playable column and the current player. Adds the player id to the board state representation.

* Is_game_over -> Doesn't receive any parameter, just checks in the current game state if there was winner player or if the game is a tie.

Definition for a winner player: A player that connects 4 of its pieces, uninterrupted, in a horizontal, vertical or diagonal line