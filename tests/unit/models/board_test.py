import pytest
import random

from src.models.board import Cell


def test_board_initialization(empty_board):
    actual = empty_board

    random_col = random.randint(0, actual.num_cols - 1)

    assert len(actual.board_state) == actual.num_cols
    assert len(actual.board_state[random_col]) == actual.num_rows

    random_row = random.randint(0, actual.num_rows - 1)
    assert type(actual.board_state[random_col][random_row]) is Cell
    assert actual.board_state[random_col][random_row] is Cell.EMPTY


def test_is_column_playable(empty_board):
    actual = empty_board
    actual.board_state[1][0] = Cell.PLAYER1
    actual.board_state[2] = [Cell.PLAYER1 for _ in actual.board_state[2]]

    assert actual.is_column_playable(0) is True
    assert actual.is_column_playable(1) is True
    assert actual.is_column_playable(2) is False
    assert actual.is_column_playable(-1) is False
    assert actual.is_column_playable(actual.num_cols) is False


def test_add_player_piece(empty_board):
    actual = empty_board
    assert actual.board_state[0][0] == Cell.EMPTY
    actual.add_piece(column=0, player_cell=Cell.PLAYER1)
    assert actual.board_state[0][0] == Cell.PLAYER1

    actual.add_piece(column=1, player_cell=Cell.PLAYER1)
    actual.add_piece(column=1, player_cell=Cell.PLAYER2)
    actual.add_piece(column=1, player_cell=Cell.PLAYER1)
    assert actual.board_state[1][0] == Cell.PLAYER1
    assert actual.board_state[1][1] == Cell.PLAYER2
    assert actual.board_state[1][2] == Cell.PLAYER1

    actual.add_piece(column=2, player_cell=Cell.PLAYER1)
    actual.add_piece(column=2, player_cell=Cell.PLAYER2)
    actual.add_piece(column=2, player_cell=Cell.PLAYER1)
    actual.add_piece(column=2, player_cell=Cell.PLAYER1)
    actual.add_piece(column=2, player_cell=Cell.PLAYER2)
    actual.add_piece(column=2, player_cell=Cell.PLAYER1)
    assert actual.board_state[2][5] == Cell.PLAYER1

    with pytest.raises(ValueError) as exception_info:
        actual.add_piece(column=2, player_cell=Cell.PLAYER2)
    assert exception_info.type is ValueError
    assert "Invalid column" in str(exception_info.value)

    with pytest.raises(ValueError) as exception_info:
        actual.add_piece(column=-1, player_cell=Cell.PLAYER2)
    assert exception_info.type is ValueError
    assert "Invalid column" in str(exception_info.value)

    with pytest.raises(ValueError) as exception_info:
        actual.add_piece(column=actual.num_cols, player_cell=Cell.PLAYER2)
    assert exception_info.type is ValueError
    assert "Invalid column" in str(exception_info.value)


def test_add_piece_returns_correct_coord(empty_board):
    actual = empty_board

    coords = actual.add_piece(column=0, player_cell=Cell.PLAYER1)
    assert coords == (0, 0)
    coords = actual.add_piece(column=1, player_cell=Cell.PLAYER1)
    assert coords == (1, 0)
    coords = actual.add_piece(column=1, player_cell=Cell.PLAYER1)
    assert coords == (1, 1)
    coords = actual.add_piece(column=1, player_cell=Cell.PLAYER1)
    assert coords == (1, 2)


def test_is_game_over_vertical(empty_board):
    actual = empty_board
    last_move = actual.add_piece(0, Cell.PLAYER1)
    assert actual.is_game_over(last_move) is False
    last_move = actual.add_piece(0, Cell.PLAYER1)
    assert actual.is_game_over(last_move) is False
    last_move = actual.add_piece(0, Cell.PLAYER1)
    assert actual.is_game_over(last_move) is False
    last_move = actual.add_piece(0, Cell.PLAYER1)
    assert actual.is_game_over(last_move) is True
    last_move = actual.add_piece(0, Cell.PLAYER1)
    assert actual.is_game_over(last_move) is True


def test_is_game_over_horizontal(empty_board):
    actual = empty_board
    last_move = actual.add_piece(0, Cell.PLAYER1)
    assert actual.is_game_over(last_move) is False
    last_move = actual.add_piece(1, Cell.PLAYER1)
    assert actual.is_game_over(last_move) is False
    last_move = actual.add_piece(2, Cell.PLAYER1)
    assert actual.is_game_over(last_move) is False
    last_move = actual.add_piece(3, Cell.PLAYER1)
    assert actual.is_game_over(last_move) is True
    last_move = actual.add_piece(4, Cell.PLAYER1)
    assert actual.is_game_over(last_move) is True


def test_is_game_over_down_left(empty_board):
    actual = empty_board
    last_move = actual.add_piece(0, Cell.PLAYER1)
    assert actual.is_game_over(last_move) is False
    last_move = actual.add_piece(1, Cell.PLAYER2)
    last_move = actual.add_piece(1, Cell.PLAYER1)
    assert actual.is_game_over(last_move) is False
    last_move = actual.add_piece(2, Cell.PLAYER2)
    last_move = actual.add_piece(2, Cell.PLAYER2)
    last_move = actual.add_piece(2, Cell.PLAYER1)
    assert actual.is_game_over(last_move) is False
    last_move = actual.add_piece(3, Cell.PLAYER2)
    last_move = actual.add_piece(3, Cell.PLAYER2)
    last_move = actual.add_piece(3, Cell.PLAYER2)
    last_move = actual.add_piece(3, Cell.PLAYER1)
    assert actual.is_game_over(last_move) is True
    last_move = actual.add_piece(4, Cell.PLAYER1)
    assert actual.is_game_over(last_move) is False


def test_is_game_over_down_right(empty_board):
    actual = empty_board
    last_move = actual.add_piece(actual.num_cols - 1, Cell.PLAYER1)
    assert actual.is_game_over(last_move) is False
    last_move = actual.add_piece(actual.num_cols - 2, Cell.PLAYER2)
    last_move = actual.add_piece(actual.num_cols - 2, Cell.PLAYER1)
    assert actual.is_game_over(last_move) is False
    last_move = actual.add_piece(actual.num_cols - 3, Cell.PLAYER2)
    last_move = actual.add_piece(actual.num_cols - 3, Cell.PLAYER2)
    last_move = actual.add_piece(actual.num_cols - 3, Cell.PLAYER1)
    assert actual.is_game_over(last_move) is False
    last_move = actual.add_piece(actual.num_cols - 4, Cell.PLAYER2)
    last_move = actual.add_piece(actual.num_cols - 4, Cell.PLAYER2)
    last_move = actual.add_piece(actual.num_cols - 4, Cell.PLAYER2)
    last_move = actual.add_piece(actual.num_cols - 4, Cell.PLAYER1)
    assert actual.is_game_over(last_move) is True
    last_move = actual.add_piece(4, Cell.PLAYER1)
    assert actual.is_game_over(last_move) is False


def test_is_game_over_up_right(empty_board):
    actual = empty_board

    last_move = actual.add_piece(1, Cell.PLAYER2)
    last_move = actual.add_piece(1, Cell.PLAYER1)
    assert actual.is_game_over(last_move) is False
    last_move = actual.add_piece(2, Cell.PLAYER2)
    last_move = actual.add_piece(2, Cell.PLAYER2)
    last_move = actual.add_piece(2, Cell.PLAYER1)
    assert actual.is_game_over(last_move) is False
    last_move = actual.add_piece(3, Cell.PLAYER2)
    last_move = actual.add_piece(3, Cell.PLAYER2)
    last_move = actual.add_piece(3, Cell.PLAYER2)
    last_move = actual.add_piece(3, Cell.PLAYER1)
    assert actual.is_game_over(last_move) is False
    last_move = actual.add_piece(0, Cell.PLAYER1)
    assert actual.is_game_over(last_move) is True
    last_move = actual.add_piece(4, Cell.PLAYER1)
    assert actual.is_game_over(last_move) is False


def test_is_game_over_up_left(empty_board):
    actual = empty_board
    last_move = actual.add_piece(actual.num_cols - 2, Cell.PLAYER2)
    last_move = actual.add_piece(actual.num_cols - 2, Cell.PLAYER1)
    assert actual.is_game_over(last_move) is False
    last_move = actual.add_piece(actual.num_cols - 3, Cell.PLAYER2)
    last_move = actual.add_piece(actual.num_cols - 3, Cell.PLAYER2)
    last_move = actual.add_piece(actual.num_cols - 3, Cell.PLAYER1)
    assert actual.is_game_over(last_move) is False
    last_move = actual.add_piece(actual.num_cols - 4, Cell.PLAYER2)
    last_move = actual.add_piece(actual.num_cols - 4, Cell.PLAYER2)
    last_move = actual.add_piece(actual.num_cols - 4, Cell.PLAYER2)
    last_move = actual.add_piece(actual.num_cols - 4, Cell.PLAYER1)
    assert actual.is_game_over(last_move) is False
    last_move = actual.add_piece(actual.num_cols - 1, Cell.PLAYER1)
    assert actual.is_game_over(last_move) is True
    last_move = actual.add_piece(4, Cell.PLAYER1)
    assert actual.is_game_over(last_move) is False


def test_is_game_over_mid_diag1(empty_board):
    actual = empty_board

    last_move = actual.add_piece(0, Cell.PLAYER1)
    assert actual.is_game_over(last_move) is False
    last_move = actual.add_piece(1, Cell.PLAYER2)
    last_move = actual.add_piece(1, Cell.PLAYER1)
    assert actual.is_game_over(last_move) is False
    last_move = actual.add_piece(2, Cell.PLAYER2)
    last_move = actual.add_piece(2, Cell.PLAYER2)
    assert actual.is_game_over(last_move) is False
    last_move = actual.add_piece(3, Cell.PLAYER2)
    last_move = actual.add_piece(3, Cell.PLAYER2)
    last_move = actual.add_piece(3, Cell.PLAYER2)
    last_move = actual.add_piece(3, Cell.PLAYER1)
    assert actual.is_game_over(last_move) is False
    last_move = actual.add_piece(2, Cell.PLAYER1)
    assert actual.is_game_over(last_move) is True
    last_move = actual.add_piece(4, Cell.PLAYER1)
    assert actual.is_game_over(last_move) is False

def test_is_game_over_mid_diag2(empty_board):
    actual = empty_board
    last_move = actual.add_piece(actual.num_cols - 1, Cell.PLAYER1)
    assert actual.is_game_over(last_move) is False
    last_move = actual.add_piece(actual.num_cols - 2, Cell.PLAYER2)
    last_move = actual.add_piece(actual.num_cols - 2, Cell.PLAYER1)
    assert actual.is_game_over(last_move) is False
    last_move = actual.add_piece(actual.num_cols - 3, Cell.PLAYER2)
    last_move = actual.add_piece(actual.num_cols - 3, Cell.PLAYER2)
    assert actual.is_game_over(last_move) is False
    last_move = actual.add_piece(actual.num_cols - 4, Cell.PLAYER2)
    last_move = actual.add_piece(actual.num_cols - 4, Cell.PLAYER2)
    last_move = actual.add_piece(actual.num_cols - 4, Cell.PLAYER2)
    last_move = actual.add_piece(actual.num_cols - 4, Cell.PLAYER1)
    assert actual.is_game_over(last_move) is False
    last_move = actual.add_piece(actual.num_cols - 3, Cell.PLAYER1)
    assert actual.is_game_over(last_move) is True
    last_move = actual.add_piece(4, Cell.PLAYER1)
    assert actual.is_game_over(last_move) is False

# def test_board_printing(self):
#     board = Board(2, 2)
#     row_string_start = "\n \033[4m" + "|"
#     row_string_end = "\033[0m"
#     row = row_string_start + "   |   |" + row_string_end
#     expected = "\n.  A   B " + row + row

#     self.assertEqual(str(board), expected)
