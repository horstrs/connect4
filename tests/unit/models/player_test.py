from unittest.mock import MagicMock
from src.models.player import Player


def test_player_delegates_to_strategy():
    mock_strategy = MagicMock()
    mock_strategy.get_move.return_value = 4

    player = Player(id=1, name="TestBot", move_strategy=mock_strategy)
    mock_board = MagicMock()  # Mock the board too

    result = player.get_move(mock_board)

    assert result == 4
    mock_strategy.get_move.assert_called_once_with(mock_board)
