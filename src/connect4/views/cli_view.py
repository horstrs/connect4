import os

from connect4.models.board import Cell
from connect4.config import (
    PLAYERS_CONFIG,
    CELL_DIVIDER,
    BOLD,
    RESET,
    COLOR_MAPPING,
    UNDERLINE,
)


class CLIView:
    def __init__(self, player_config: dict = None, color_mapping: dict = None):
        base_config = player_config if player_config is not None else PLAYERS_CONFIG
        self.player_config = self._load_player_config(base_config)
        self.color_mapping = color_mapping or COLOR_MAPPING

    def _load_player_config(self, config: dict) -> dict:
        # Ensure both players exist in whatever config was passed
        for player in [Cell.PLAYER1, Cell.PLAYER2]:
            if player.value not in config:
                raise AttributeError(f"Missing configuration for player {player}")
        return config

    def _convert_cell_data_to_player_config(self, cell_data: int) -> str:
        if cell_data == Cell.EMPTY.value:
            return "   "

        current_player_config = self.player_config.get(cell_data)
        color_name = current_player_config.get("COLOR", "").lower()
        ansi_code = COLOR_MAPPING.get(color_name, "")
        shape = current_player_config.get("SHAPE", " ").upper()

        if shape.strip():
            return f"{BOLD}{UNDERLINE}{ansi_code} {shape} {RESET}"

        bg_ansi = COLOR_MAPPING.get(f"bg_{color_name}", ansi_code)
        return f"{bg_ansi}   {RESET}"

    def _get_player_ansi_color(self, player_id: int) -> str:
        config = self.player_config.get(player_id, {})
        color_name = config.get("COLOR", "").lower()
        return COLOR_MAPPING.get(color_name, "")

    def print_board(self, board_state: list[list[Cell]]) -> str:
        rows = []
        for r in reversed(range(len(board_state[0]))):
            row_data = [
                self._convert_cell_data_to_player_config(board_state[c][r])
                for c in range(len(board_state))
            ]
            rows.append(
                f"{UNDERLINE}{CELL_DIVIDER}"
                + f"{UNDERLINE}{CELL_DIVIDER}".join(row_data)
                + f"{UNDERLINE}{CELL_DIVIDER}{RESET}"
            )
        floor = "-" * (len(board_state) * 4 + 1)
        head_foot = "  " + "   ".join([str(i) for i in range(len(board_state))])
        board = "\n".join(rows) + "\n" + floor
        print("\n" + head_foot + "\n" + board + "\n" + head_foot)

    def get_user_input(self, player_name: str) -> int:
        print(f"\n{player_name}'s turn.")
        val = input("\nSelect a column to play: ")
        try:
            return int(val)
        except ValueError:
            return -1

    def print_error_message(self, message: str) -> None:
        red = COLOR_MAPPING.get("red", "")
        print(f"{BOLD}{red}>> {message}{RESET}")

    def print_game_over_screen(self, message: str, player_id: int = 0) -> None:
        ansi_color = self._get_player_ansi_color(player_id)
        print(f"\n{ansi_color}{message}{RESET}")

    def clear_screen(self):
        if os.name == "nt":
            _ = os.system("cls")
        else:
            _ = os.system("clear")
