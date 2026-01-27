import pytest
import copy

from src.models.board import Board, Cell
from src.models.player import Player
from src.models.player_strategies import HumanStrategy  # , RandomAIStrategy


@pytest.fixture
def empty_board():
    """Returns a fresh 6x7 board for every test."""
    return Board(num_rows=6, num_cols=7)


@pytest.fixture
def human_player():
    """Returns a standard human player instance."""
    return Player(player_id=1, name="Human", move_strategy=HumanStrategy())


@pytest.fixture
def full_board(empty_board):
    full_board = copy.deepcopy(empty_board)

    for column in range(full_board.num_cols):
        for _ in range(full_board.num_rows):
            full_board.add_piece(column, Cell.PLAYER1)
    return full_board


# @pytest.fixture
# def ai_player():
#     """Returns a standard AI player instance."""
#     return Player(player_id=2, name="Robo", move_strategy=RandomAIStrategy())
