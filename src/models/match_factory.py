from src.models.board import Board, Cell
from src.models.player import Player
from src.models.player_strategies import HumanStrategy, RandomBotStrategy


class MatchFactory:
    @staticmethod
    def setup_classic_pvp(
        p1name: str = "Human Player 1", p2name: str = "Human Player 2"
    ):
        board = Board(7, 6)
        p1 = Player(Cell.PLAYER1, p1name, HumanStrategy())
        p2 = Player(Cell.PLAYER2, p2name, HumanStrategy())
        return board, [p1, p2]

    @staticmethod
    def setup_classic_random_vs_random(
        p1name: str = "Random Bot 1", p2name: str = "Random Bot 2"
    ):
        board = Board(7, 6)
        p1 = Player(Cell.PLAYER1, p1name, RandomBotStrategy())
        p2 = Player(Cell.PLAYER2, p2name, RandomBotStrategy())
        return board, [p1, p2]
