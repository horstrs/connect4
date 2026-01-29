import random
import time

from abc import ABC, abstractmethod
from src.models.board import Board

class MoveStrategy(ABC):
    @abstractmethod
    def get_move(self, board: Board) -> int:
        """
        Generates the next column for player move given a board state.
        If player is Human, then the return should be a signal for the controller to ask user input from View
        """


class HumanStrategy(MoveStrategy):
    def get_move(self, board: Board) -> int:
        """
        No move logic, just return a constant to signal the controller that user input is required
        """
        raise RuntimeError("Controller should call view to get human move")


class RandomBotStrategy(MoveStrategy):
    def get_move(self, board: Board) -> int:
        time.sleep(0.1)
        valid_columns = [c for c in range(board.num_cols) if board.is_column_playable(c)]
        return random.choice(valid_columns)