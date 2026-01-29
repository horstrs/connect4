from unittest.mock import MagicMock
from models.player_strategies import HumanStrategy, RandomBotStrategy


def test_human_strategy_get_move():
    human = HumanStrategy()
    mock_board = MagicMock()
    try:
        human.get_move(mock_board)
        assert False
    except RuntimeError as exc:
        assert str(exc) == "Controller should call view to get human move"


def test_random_bot_strategy_get_move():
    random_bot = RandomBotStrategy()
    mock_board = MagicMock()
    mock_board.num_cols = 7

    mock_board.is_column_playable.side_effect = lambda c: c in [0, 4]
    for _ in range(30):
        result = random_bot.get_move(mock_board)
        assert result in (0, 4)
        assert result not in ( 1, 2, 3, 5, 6)
