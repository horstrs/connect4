from src.models.board import Cell
from src.config import PLAYERS_CONFIG, CELL_DIVIDER, BOLD, RESET, COLOR_MAPPING


class CLIView:
    def __init__(self):
        self.name = ""

    def _convert_cell_data_to_player_config(self, cell_data: int) -> str:
        if cell_data == Cell.EMPTY.value:
            return "   "

        player_config = PLAYERS_CONFIG.get(cell_data)
        if not player_config or player_config is None:
            raise AttributeError(f"Missing configuration for player {cell_data}")

        color_name = player_config.get("COLOR")
        ansi_code = COLOR_MAPPING.get(color_name, "")
        shape = player_config.get("SHAPE", " ").upper()

        if shape.strip():
            return f"{BOLD}{ansi_code} {shape} {RESET}"
        
        bg_ansi = COLOR_MAPPING.get(f"bg_{color_name}", ansi_code)
        return f"{bg_ansi}   {RESET}"

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

    def get_user_input(self):  # TODO: Change implementation to get input from user
        print("Select a column to play:")
        pass
