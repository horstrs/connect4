class Player:
    def __init__(self, player_id, name, move_strategy):
        self.player_id = player_id
        self.name = name
        self.move_strategy = move_strategy
        # self.score = 0 #TODO implement further if AI vs AI analytical becomes relevant

    def get_move(self, board) -> int | str:
        return self.move_strategy.calculate_move(board)
