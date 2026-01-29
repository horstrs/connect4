from src.models.board import Cell
from src.config import PLAYERS_CONFIG, CELL_DIVIDER, BOLD, RESET, COLOR_MAPPING


class CLIView:
    def __init__(self):
        self.player_config = self._load_player_config()

    def _load_player_config(self) -> dict:
        player_config = PLAYERS_CONFIG.get(Cell.PLAYER1)
        if not player_config or player_config is None:
            raise AttributeError(f"Missing configuration for player {Cell.PLAYER1}")

        player_config = PLAYERS_CONFIG.get(Cell.PLAYER2)
        if not player_config or player_config is None:
            raise AttributeError(f"Missing configuration for player {Cell.PLAYER2}")

        return PLAYERS_CONFIG

    def _convert_cell_data_to_player_config(self, cell_data: int) -> str:
        if cell_data == Cell.EMPTY.value:
            return "   "

        current_player_config = self.player_config.get(cell_data)
        color_name = current_player_config.get("COLOR")
        ansi_code = COLOR_MAPPING.get(color_name, "")
        shape = current_player_config.get("SHAPE", " ").upper()

        if shape.strip():
            return f"{BOLD}{ansi_code} {shape} {RESET}"

        bg_ansi = COLOR_MAPPING.get(f"bg_{color_name}", ansi_code)
        return f"{bg_ansi}   {RESET}"

    def _get_player_ansi_color(self, player_id: int) -> str:
        if player_id == Cell.EMPTY.value:
            return ""
        current_player_config = self.player_config.get(player_id)
        color_name = current_player_config.get("COLOR")
        ansi_code = COLOR_MAPPING.get(color_name, "")
        return ansi_code

    def print_board(self, board_state: list[list[Cell]]) -> str:
        rows = []
        for r in reversed(range(len(board_state[0]))):
            row_data = [
                self._convert_cell_data_to_player_config(board_state[c][r])
                for c in range(len(board_state))
            ]
            rows.append(
                f"{CELL_DIVIDER}" + f"{CELL_DIVIDER}".join(row_data) + f"{CELL_DIVIDER}"
            )
        floor = "-" * (len(board_state) * 4 + 1)
        head_foot = "  " + "   ".join([str(i) for i in range(len(board_state))])
        board = "\n".join(rows) + "\n" + floor
        print("\n" + head_foot + "\n" + board + "\n" + head_foot)

    def get_user_input(self, player_name: str) -> int:
        print(f"\n{player_name}'s turn.")
        val = input("Select a column to play:")
        try:
            return int(val)
        except ValueError:
            return -1

    def print_error_message(self, message: str) -> None:
        red = COLOR_MAPPING.get("red", "")
        print(f"{BOLD}{red}>> {message}{RESET}")

    def print_game_over_screen(self, message: str, player_id: int = 0) -> None:
        ansi_color = self._get_player_ansi_color(player_id)
        print(f"{ansi_color}{message}{RESET}")
