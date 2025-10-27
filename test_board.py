import unittest
import random

from board import Board, PlayerPiece, Cell


class TestBoard(unittest.TestCase):
    def test_board_initialization(self):
        num_rows = 6
        num_cols = 7
        actual = Board(num_rows, num_cols)

        random_row = random.randint(0, num_rows-1)

        self.assertEqual(len(actual.board_state), num_rows)
        self.assertEqual(len(actual.board_state[random_row]), num_cols)
        
        random_col = random.randint(0, num_cols-1)
        self.assertEqual(type(actual.board_state[random_row][random_col]), PlayerPiece)
        self.assertEqual(actual.board_state[random_row][random_col].p1p2, Cell.EMPTY)
        
        self.assertEqual(str(actual.board_state[random_row][random_col]), "   ")


    def test_board_printing(self):
        board = Board(2, 2)
        row_string_start = "\n \033[4m" + "|"
        row_string_end = "\033[0m"
        row = row_string_start + "   |   |" + row_string_end
        expected = "\n.  A   B " + row + row

        self.assertEqual(str(board), expected)

if __name__ == "__main__":
    unittest.main()
