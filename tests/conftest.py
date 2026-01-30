import pytest
import copy

from itertools import cycle
from unittest.mock import MagicMock
from connect4.controllers.game_manager import GameManager
from connect4.models.board import Board, Cell
from connect4.models.player import Player
from connect4.models.player_strategies import HumanStrategy
from connect4.views.cli_view import CLIView


@pytest.fixture
def empty_board():
    """Returns a fresh 6x7 board for every test."""
    return Board(num_rows=6, num_cols=7)


@pytest.fixture
def human_player():
    """Returns a standard human player instance."""
    return Player(id=1, name="Human", move_strategy=HumanStrategy())


@pytest.fixture
def full_board(empty_board):
    full_board = copy.deepcopy(empty_board)
    first_half = int(full_board.num_rows / 2)
    second_half = full_board.num_rows - first_half
    iterator = cycle([Cell.PLAYER1, Cell.PLAYER2])
    for column in range(full_board.num_cols):
        for _ in range(first_half):
            full_board.add_piece(column, next(iterator))
    next(iterator)
    for column in range(full_board.num_cols):
        for _ in range(second_half):
            full_board.add_piece(column, next(iterator))

    return full_board


@pytest.fixture
def view_mock():
    return MagicMock()


@pytest.fixture
def board_mock():
    return MagicMock()


@pytest.fixture
def players():
    p1 = MagicMock()
    p2 = MagicMock()
    return [p1, p2]


@pytest.fixture
def manager(view_mock, board_mock, players):
    return GameManager(view_mock, board_mock, players)


@pytest.fixture
def board_to_tie(full_board):
    board_to_tie = copy.deepcopy(full_board)
    board_to_tie.board_state[0][-1] = Cell.EMPTY
    return board_to_tie


@pytest.fixture
def board_to_win(empty_board):
    almost_won_board = copy.deepcopy(empty_board)
    almost_won_board.add_piece(0, Cell.PLAYER1)
    almost_won_board.add_piece(0, Cell.PLAYER1)
    almost_won_board.add_piece(0, Cell.PLAYER1)
    return almost_won_board


@pytest.fixture
def fake_color_mapping():
    return {
        "red": "\033[31m",
        "yellow": "\033[33m",
        "bg_red": "\033[41m",
        "bg_yellow": "\033[43m",
        "reset": "\033[0m",
        "bold": "\033[1m",
    }


@pytest.fixture
def fake_player_config():
    return {
        Cell.PLAYER1.value: {"COLOR": "red", "SHAPE": "X"},
        Cell.PLAYER2.value: {"COLOR": "yellow", "SHAPE": ""},
    }


@pytest.fixture
def view(fake_player_config, fake_color_mapping):
    return CLIView(player_config=fake_player_config, color_mapping=fake_color_mapping)
