from ..config import ROWS, COLUMNS
from ..models.board import Board

class BoardCLI:
    def __init__(self):
        self.board_header = self.__initialize_board_header__()
        self.num_rows = ROWS
        self.num_cols = COLUMNS

    def __initialize_board_header__(self):
        last_letter_index = self.num_cols + ord("A")
        board_header = "."
        for letter_ord in range(ord("A"), last_letter_index):
            board_header += f"  {chr(letter_ord)} "
        return board_header

    def print_board(self, board: Board) -> None:
        pass


# def __repr__(self):
#         board_header = "\n" + self.board_header
#         row_string_start = "\n \033[4m" + CELL_DIVIDER
#         row_string_end = "\033[0m"
#         all_rows = ""
#         for row in self.board_state:
#             row_string = ""
#             for column in row:
#                 row_string += str(column) + CELL_DIVIDER
#             all_rows += row_string_start + row_string + row_string_end
#         return board_header + all_rows
