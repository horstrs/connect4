import string

from itertools import cycle
from src.models.board import Board, Cell
from src.config import COLUMNS, ROWS


def main():
    print("Welcome to Connect4!")
    # TODO: Add a call to controller class that handles Start Menu (initialize Configs) and call display start menu from a view class
    # TODO: Move this logic to a controller class to instantiate a new game
    board = Board(COLUMNS, ROWS)
    players = cycle([Cell.PLAYER1, Cell.PLAYER2])

    # TODO: Move this logic to the view class to print the board
    print(board)
    current_player = next(players)
    print(current_player)

    wait_for_input = True
    while wait_for_input:
        player_selection = int(input("Choose a column to add a piece (0 - 6): "))
        if not board.is_column_playable(player_selection):
            print("invalid entry!")
            continue

        
        player_move = board.add_piece(player_selection, current_player)
        print(board)
        if board.has_player_won(player_move):
            print(f"Game is over! Player {current_player} won!")
            wait_for_input = False
        current_player = next(players)
        


def is_valid(player_selection: str, board: Board) -> bool:
    column_names = string.ascii_uppercase[:COLUMNS]

    if player_selection not in column_names:
        print("Column not listed in header")
        return False

    # column_index = board.header_indexes[player_selection]

    # if board.is_column_full(column_index):
    # print(f"Column {player_selection} is already full")
    # return False

    return True


if __name__ == "__main__":
    main()
