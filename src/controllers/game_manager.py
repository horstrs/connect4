from itertools import cycle
from models.board import Board
from models.player import Player
from views.cli_view import CLIView


class GameManager:
    def __init__(self, view: CLIView, board: Board, players: list[Player]):
        self.view = view
        self.game_board = board
        self.player1 = players[0]
        self.player2 = players[1]
        self.players_iterator = cycle([self.player1, self.player2])

    def _handle_turn(self, current_player: Player):
        game_ended = False
        next_move = self._get_move(current_player)
        while not self.game_board.is_column_playable(next_move):
            self.view.print_error_message("invalid move")
            self.view.print_board(self.game_board.board_state)

            next_move = self._get_move(current_player)

        board_coord = self.game_board.add_piece(next_move, current_player.id)
        if self.game_board.has_player_won(board_coord):
            self.view.print_game_over_screen(
                f"Game Over! {current_player.name} has won", current_player.id
            )

            game_ended = True
            return game_ended
        if self.game_board.is_tie():
            self.view.print_game_over_screen("Game Over! It's a tie!")
            game_ended = True
            return game_ended

        return game_ended

    def _get_move(self, current_player: Player):
        if current_player.is_human():
            return self.view.get_user_input(current_player.name)
        else:
            return current_player.get_move(self.game_board)

    def game_loop(self):
        game_ended = False

        while not game_ended:
            current_player = next(self.players_iterator)
            self.view.print_board(self.game_board.board_state)
            game_ended = self._handle_turn(current_player)

        self.view.print_board(self.game_board.board_state)
