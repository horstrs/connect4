from unittest.mock import MagicMock, patch
from connect4.models.player import Player

def test_manager_initialization(manager, view_mock, board_mock, players):
    assert manager.view == view_mock
    assert manager.game_board == board_mock
    assert manager.player1 == players[0]
    assert manager.player2 == players[1]
    first = next(manager.players_iterator)
    second = next(manager.players_iterator)
    third = next(manager.players_iterator)
    assert first == players[0]
    assert second == players[1]
    assert third == players[0]


def test_handle_turn_player_won(manager):
    manager.game_board.is_column_playable.return_value = True
    manager.game_board.has_player_won.return_value = True
    manager.player1.is_human.return_value = True
    manager.view.get_user_input.return_value = 0

    result = manager._handle_turn(manager.player1)

    assert result is True
    manager.game_board.add_piece.assert_called_once()
    manager.game_board.has_player_won.assert_called_once()
    manager.game_board.is_tie.assert_not_called()
    manager.player1.is_human.assert_called_once()
    manager.view.get_user_input.assert_called_once()


def test_handle_turn_game_tied(manager):
    manager.game_board.is_column_playable.return_value = True
    manager.game_board.has_player_won.return_value = False
    manager.game_board.is_tie.return_value = True
    manager.player1.is_human.return_value = False
    manager.player1.get_move.return_value = 0

    result = manager._handle_turn(manager.player1)

    assert result is True
    manager.game_board.add_piece.assert_called_once()
    manager.game_board.has_player_won.assert_called_once()
    manager.game_board.is_tie.assert_called_once()
    manager.player1.is_human.assert_called_once()
    manager.player1.get_move.assert_called_once()


def test_handle_turn_game_not_finished(manager):
    manager.game_board.is_column_playable.return_value = True
    manager.game_board.has_player_won.return_value = False
    manager.game_board.is_tie.return_value = False
    manager.player1.is_human.return_value = False
    manager.player1.get_move.return_value = 0

    result = manager._handle_turn(manager.player1)

    assert result is False
    manager.game_board.add_piece.assert_called_once()
    manager.game_board.has_player_won.assert_called_once()
    manager.game_board.is_tie.assert_called_once()
    manager.player1.is_human.assert_called_once()
    manager.player1.get_move.assert_called_once()


def test_ask_for_player_input(manager):
    # with patch.object(manager.game_board, "is_column_playable") as mock_column_playable:
    manager.game_board.is_column_playable.side_effect = [False, True]
    manager.player1.is_human.return_value = True
    user_inputs = [99, 3]
    manager.view.get_user_input.side_effect = user_inputs
    manager.game_board.has_player_won.return_value = False
    manager.game_board.is_tie.return_value = False

    result = manager._handle_turn(manager.player1)

    assert result is False
    manager.view.print_error_message.assert_called_once_with(f"{user_inputs[0]} is an invalid move")
    manager.view.print_board.assert_called_once()
    assert manager.view.get_user_input.call_count == 2
    assert manager.game_board.is_column_playable.call_count == 2


# def test_handle_turn_reaches_while_loop(manager, board_mock, view_mock):
#     # Reset mocks to clear any previous test pollution
#     board_mock.reset_mock()
#     view_mock.reset_mock()

#     # FORCE the logic path
#     # 1. First call fails, second call succeeds
#     board_mock.is_column_playable.side_effect = [False, True]

#     # 2. Mock a human player so it goes through the view
#     human = MagicMock(spec=Player)
#     human.is_human.return_value = True
#     human.name = "TestPlayer"
#     human.id = 1

#     # 3. View returns two values: one to enter loop, one to exit
#     view_mock.get_user_input.side_effect = [5, 5]

#     # 4. Prevent win/tie from exiting early
#     board_mock.has_player_won.return_value = False
#     board_mock.is_tie.return_value = False

#     # ACT
#     manager._handle_turn(human)

#     # ASSERT - If these pass, coverage MUST be 100%
#     assert board_mock.is_column_playable.call_count == 2
#     view_mock.print_error_message.assert_called_with("invalid move")
#     view_mock.print_board.assert_called()


def test_game_loop(manager):
    manager._handle_turn = MagicMock(return_value=True)
    manager.game_loop()
    manager._handle_turn.assert_called()
    manager._handle_turn.assert_called_once()


def test_game_loop_switches_players_and_continues(manager):
    with patch.object(manager, "_handle_turn") as mock_handle:
        mock_handle.side_effect = [False, True]

        manager.game_loop()

        assert mock_handle.call_count == 2

        calls = mock_handle.call_args_list
        assert calls[0].args[0] == manager.player1
        assert calls[1].args[0] == manager.player2
