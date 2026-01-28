from src.models.player_strategies import MoveStrategy

class Player:
    def __init__(self, id: int, name: str, move_strategy: MoveStrategy):
        self.id = id
        self.name = name
        self.move_strategy = move_strategy
        # self.score = 0 #TODO implement further if AI vs AI analytical becomes relevant

    def get_move(self, board) -> int | str:
        return self.move_strategy.get_move(board)
