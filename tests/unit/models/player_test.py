from unittest.mock import MagicMock
from src.models.player import Player
from src.models.player_strategies import HumanStrategy, RandomBotStrategy

def test_player_delegates_to_strategy():
    mock_strategy = MagicMock()
    mock_strategy.get_move.return_value = 4

    player = Player(id=1, name="TestBot", move_strategy=mock_strategy)
    mock_board = MagicMock()  # Mock the board too

    result = player.get_move(mock_board)

    assert result == 4
    mock_strategy.get_move.assert_called_once_with(mock_board)


def test_player_is_human():
    human = Player(id=1, name="HumanPlayer", move_strategy=HumanStrategy())
    bot = Player(id=2, name="Bot", move_strategy=RandomBotStrategy())

    assert human.is_human() is True
    assert bot.is_human() is False