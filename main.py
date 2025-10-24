from board import Board
from config import ROWS, COLUMNS

def main():
    print("Welcome to Connect4!")
    #print_board()
    board = Board(ROWS, COLUMNS)
    print(board)
    


if __name__ == "__main__":
    main()
