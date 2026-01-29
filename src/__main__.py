from models.match_factory import MatchFactory
from controllers.game_manager import GameManager
from views.cli_view import CLIView


def main():
    print("Welcome to Connect4!")

    view = CLIView()
    board, players = MatchFactory.setup_classic_player_vs_random()
    # board, players = MatchFactory.setup_classic_random_vs_random()
    # board, players = MatchFactory.setup_classic_pvp()
    game_manager = GameManager(view, board, players)
    game_manager.game_loop()


if __name__ == "__main__":
    main()
