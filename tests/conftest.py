import pytest
import copy

from itertools import cycle
from unittest.mock import MagicMock
from src.controllers.game_manager import GameManager
from src.models.board import Board, Cell
from src.models.player import Player
from src.models.player_strategies import HumanStrategy, RandomBotStrategy


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
    # p1 = Player(Cell.PLAYER1, "P1", HumanStrategy())
    # p2 = Player(Cell.PLAYER2, "P2", RandomBotStrategy())
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


# @pytest.fixture
# def ai_player():
#     """Returns a standard AI player instance."""
#     return Player(player_id=2, name="Robo", move_strategy=RandomAIStrategy())
