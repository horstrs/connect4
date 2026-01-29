from src.models.match_factory import MatchFactory
from src.controllers.game_manager import GameManager
from src.views.cli_view import CLIView


def main():
    print("Welcome to Connect4!")

    view = CLIView()
    # board, players = MatchFactory.setup_classic_pvp()
    board, players = MatchFactory.setup_classic_random_vs_random()
    game_manager = GameManager(view, board, players)
    game_manager.game_loop()


if __name__ == "__main__":
    main()
