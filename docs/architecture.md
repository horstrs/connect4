# GameManager class (Controller):

1. Start new game, instantiate an empty board and player 1 and player 2.
Here is the start of the game loop:
1. Use View to ask for user input and capture it
1. Input (View): The View captures the raw input, validate if format is correct (e.g., transform column "A" to index 0, or make sure that user didn't enter invalid info, like "random_string") and passes it back to the Controller.
1. Validation against game logic (Controller): The Controller asks the Model if that column is playable. If not, go back to step 2. If it is, proceed.
1. Update (Model): The Controller tells the Model to drop a piece. The Model updates its internal state and returns the result (a tuple with the (col, row) coordinate of the move).
1. Render (View): The Controller sends the updated board data to the View to be printed.
1. Win/Tie Check (Model): The Controller asks the Model if the last move triggered a win. If not, check if it's a draw. If either has happened, ask the view to print end of game screen. Otherwise, go back to first game loop step

Note: The View never asks the Model for data; the Controller acts as the middleman.

# Player class:
Contains the player id, player name and the move strategy.

This class has a `get_move(board)` method, that should use the `move_strategy` instance to decide the next move. 

The move strategies currently implemented are:
* `HumanStrategy`: It's implementation of get_move() should never be directly called, since the controller is supposed to get the move from the view by asking the human player for input. So it just raises an error to make sure it's not called.

* `RandomBotStrategy`: It gets a list of columns available and choses randomly one of them


# Board class:

The board should contain the number of rows and columns and a living board state, that's initialized in the constructor.
The `board_state` is just a list of lists, where the outter list represents the columns and the inner list represents the lines. And each cell would contain either 0 for empty cells, or 1 or 2 representing player 1 and player 2, respectively.

The methods needed for the board class are:

* Is_column_playable -> Receives a column indexes and if the index exists and is not yet full return True. Otherwise, return false

* Add piece -> Receives a playable column and the current player. Adds the player id to the board state representation.

* Is_game_over -> Doesn't receive any parameter, just checks in the current game state if there was winner player or if the game is a tie.

    * Definition for a winner player: A player that connects 4 of its pieces, uninterrupted, in a horizontal, vertical or diagonal line
    * Definition for a tie: Top cell for all columns are filled

# View Class

The CLI print implementation is done here. It receives a config dictionary that maps the color and shape chosen by each player. The shape and color will be used when printting the board in the CLI.
If no shape is chosen, then the full color is printed as background instead.
The view is also responsible for getting the input from a human player. If the player enters a value that's not a column, it will inform it's an incorrect value and ask for input again.

Next steps for view:
* New game menu, where player can choose:
    * Type of match (PVP, PVE or EVE)
    * If match agains bot (PVE or EVE), then player can choose bot types once other move strategies are implemented
    * Config changes - so player doesn't have to change config files manually
    * Exit game

* End game screen, where player can choose to play again against the same opponent or go back to main screen or exit game

* Update ingame screen with round number