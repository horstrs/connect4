from abc import ABC, abstractmethod

NEED_USER_INPUT = "NEED_USER_INPUT"


class MoveStrategy(ABC):
    @abstractmethod
    def get_move(self, board_state: list[list[int]]) -> int | str:
        """
        Generates the next column for player move given a board state.
        If player is Human, then the return should be a signal for the controller to ask user input from View
        """


class HumanStrategy(MoveStrategy):
    def get_move(self, board_state: list[list[int]]) -> str:
        """
        No move logic, just return a constant to signal the controller that user input is required
        """
        return NEED_USER_INPUT
