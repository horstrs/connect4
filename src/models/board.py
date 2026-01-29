from enum import IntEnum


class Cell(IntEnum):
    EMPTY = 0
    PLAYER1 = 1
    PLAYER2 = 2


class Board:
    def __init__(self, num_cols, num_rows):
        self.num_cols = num_cols
        self.num_rows = num_rows
        self.board_state = self._initialize_board_state()

    def __str__(self):
        rows = []
        for r in reversed(range(self.num_rows)):
            # Get the cell value for each column in this row
            row_data = [str(self.board_state[c][r].value) for c in range(self.num_cols)]
            rows.append("| " + " | ".join(row_data) + " |")

        # Add a floor to the board
        floor = "-" * (self.num_cols * 4 + 1)
        return "\n".join(rows) + "\n" + floor

    def __repr__(self):
        return f"Board({self.num_cols}x{self.num_rows})\n{self.__str__()}"

    def _initialize_board_state(self) -> list[list[Cell]]:
        board = [
            [Cell.EMPTY for _ in range(self.num_rows)] for _ in range(self.num_cols)
        ]
        return board

    def _is_column_full(self, column: int) -> bool:
        top_row = self.board_state[column][-1]
        if top_row == Cell.EMPTY:
            return False
        return True

    def _verify_vertical_win(self, last_move: tuple[int, int]) -> bool:
        column, row = last_move
        player = self.board_state[column][row]
        NUM_TILES_BELOW = 3
        if row < NUM_TILES_BELOW:
            return False
        verical_slice = self.board_state[column][row - NUM_TILES_BELOW : row + 1]
        if all(piece == player for piece in verical_slice):
            return True
        return False

    def _verify_horizontal_win(self, last_move: tuple[int, int]) -> bool:
        column, row = last_move
        player = self.board_state[column][row]
        WINDOW_SIZE = 4
        left = max(0, (column - WINDOW_SIZE - 1))
        right = min(self.num_cols, column + WINDOW_SIZE)
        for i in range(left, right - WINDOW_SIZE + 1):
            window = [self.board_state[c][row] for c in range(i, i + WINDOW_SIZE)]
            if all(piece == player for piece in window):
                return True

        return False

    def _verify_diag_1_win(self, last_move: tuple[int, int]) -> bool:
        column, row = last_move
        player = self.board_state[column][row]
        WINDOW_SIZE = 4

        for i in range(WINDOW_SIZE):
            start_column = column - i
            start_row = row - i

            coords = [(start_column + j, start_row + j) for j in range(WINDOW_SIZE)]

            if all(
                0 <= c < self.num_cols and 0 <= r < self.num_rows for c, r in coords
            ):
                window_values = [self.board_state[c][r] for c, r in coords]
                if all(piece == player for piece in window_values):
                    return True
        return False

    def _verify_diag_2_win(self, last_move: tuple[int, int]) -> bool:
        column, row = last_move
        player = self.board_state[column][row]
        WINDOW_SIZE = 4

        for i in range(WINDOW_SIZE):
            start_column = column - i
            start_row = row + i

            coords = [(start_column + j, start_row - j) for j in range(WINDOW_SIZE)]

            if all(
                0 <= c < self.num_cols and 0 <= r < self.num_rows for c, r in coords
            ):
                window_values = [self.board_state[c][r] for c, r in coords]
                if all(piece == player for piece in window_values):
                    return True
        return False

    def is_column_playable(self, column: int) -> bool:
        if column < 0 or column >= self.num_cols:
            return False
        if self._is_column_full(column):
            return False
        return True

    def add_piece(self, column: int, player_cell: Cell) -> tuple[int, int]:
        if not self.is_column_playable(column):
            raise ValueError("Invalid column")
        first_empty_row = self.board_state[column].index(Cell.EMPTY)
        self.board_state[column][first_empty_row] = player_cell
        return (column, first_empty_row)

    def has_player_won(self, last_move: tuple[int, int]) -> bool:
        return any(
            check(last_move)
            for check in (
                self._verify_vertical_win,
                self._verify_horizontal_win,
                self._verify_diag_1_win,
                self._verify_diag_2_win,
            )
        )

    def is_tie(self) -> bool:
        return all([self._is_column_full(column) for column in range(self.num_cols)])
