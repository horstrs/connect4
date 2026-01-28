from itertools import cycle
from src.models.board import Board
from src.models.player import Player
from src.views.cli_view import CLIView


class GameManager:
    def __init__(self, view: CLIView, board: Board, players: list[Player]):
        self.view = view
        self.game_board = board
        self.player1 = players[0]
        self.player2 = players[1]
        self.players_iterator = cycle([self.player1, self.player2])

    def _handle_turn(self, current_player):
        game_ended = False
        next_move = self.view.get_input()
        while not self.game_board.is_column_playable(next_move):
            print("invalid move")  # TODO: Implement print in view class
            next_move = self.view.get_input()  # TODO: Implement get_input in view class

        board_coord = self.game_board.add_piece(next_move, current_player.id)
        if self.game_board.has_player_won(board_coord):
            print(
                f"Game Over! {current_player.name} has won"
            )  # TODO: Move this to View class
            game_ended = True
            return game_ended
        if self.game_board.is_tie():
            print("Game Over! It's a tie!")  # TODO: Move this to View class
            game_ended = True
            return game_ended

        return game_ended

    def game_loop(self):
        game_ended = False

        while not game_ended:
            current_player = next(self.players_iterator)
            # self.view.render_board(self.game_board) #TODO: Implemente board rendering in view
            print(self.game_board)
            game_ended = self._handle_turn(current_player)

        # self.view.render_board(self.game_board) #TODO: Implemente board rendering in view
        print(self.game_board)
