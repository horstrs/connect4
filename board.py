from enum import Enum
from config import CELL_DIVIDER


class Cell(Enum):
    EMPTY = " "
    PLAYER1 = 1
    PLAYER2 = 2


class PlayerPiece:
    def __init__(self, p1p2, color="RED"):
        self.p1p2 = p1p2
        self.color = color

    def __str__(self):
        match self.p1p2:
            case Cell.EMPTY:
                return "   "
            case Cell.PLAYER1:
                return " X "
            case Cell.PLAYER2:
                return " 0 "


class Board:
    def __init__(self, num_rows, num_cols):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.board_header = self.__initialize_board_header__()
        self.board_state = self.__initialize_board_state__()

    def __initialize_board_header__(self):
        last_letter_index = self.num_cols + ord("A")
        board_header = "."
        for letter_ord in range(ord("A"), last_letter_index):
            board_header += f"  {chr(letter_ord)} "
        return board_header

    def __initialize_board_state__(self):
        column = [PlayerPiece(Cell.EMPTY)] * self.num_cols
        board = [column] * self.num_rows

        return board

    def __repr__(self):
        board_header = "\n" + self.board_header
        row_string_start = "\n \033[4m" + CELL_DIVIDER
        row_string_end = "\033[0m"
        all_rows = ""
        for row in self.board_state:
            row_string = ""
            for column in row:
                row_string += str(column) + CELL_DIVIDER
            all_rows += row_string_start + row_string + row_string_end
        return board_header + all_rows
