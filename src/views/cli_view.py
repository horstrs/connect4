from src.models.board import Cell
from src.config import PLAYERS_CONFIG, CELL_DIVIDER


COLOR_CODES = {
    "empty": {},
    "foreground": {
        "black": "\033[30m",
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m",
    },
    "background": {
        "black": "\033[40m",
        "red": "\033[41m",
        "green": "\033[42m",
        "yellow": "\033[43m",
        "blue": "\033[44m",
        "magenta": "\033[45m",
        "cyan": "\033[46m",
        "white": "\033[47m",
    },
}
BOLD = "\033[1m"
RESET = "\033[0m"


class CLIView:
    def __init__(self):
        self.name = ""

    def _convert_cell_data_to_player_config(self, cell_data: int) -> str:
        if cell_data == Cell.EMPTY.value:
            return "   "

        player_config = PLAYERS_CONFIG.get(cell_data)
        if not player_config or player_config is None:
            raise AttributeError(f"Missing configuration for player {cell_data}")

        if player_config["SHAPE"] and player_config["SHAPE"] != "":
            return (
                BOLD
                + COLOR_CODES["foreground"][player_config["COLOR"]]
                + f" {player_config['SHAPE'].upper()} "
                + RESET
            )

        return COLOR_CODES["background"][player_config["COLOR"]] + "   " + RESET

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
        board = "\n".join(rows) + "\n" + floor
        print(board)

    def get_user_input(self):  # TODO: Change implementation to get input from user
        print("Select a column to play:")
        pass
