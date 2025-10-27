from board import Board
from config import ROWS, COLUMNS

def main():
    print("Welcome to Connect4!")
    #print_board()
    board = Board(ROWS, COLUMNS)
    print(board)
    wait_for_input = True
    while wait_for_input:
        player_selection = input("Choose a column to add a piece (A - G): ")
        if len(player_selection) != 1:
            print("invalid entry!")
        else:
            wait_for_input = False
        


if __name__ == "__main__":
    main()
