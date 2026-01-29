from unittest.mock import MagicMock, patch


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


def test_game_loop(manager):
    manager._handle_turn = MagicMock(return_value=True)
    manager.game_loop()
    manager._handle_turn.assert_called()
    manager._handle_turn.assert_called_once()


def test_game_loop_switches_players_and_continues(manager, board_mock):
    with patch.object(manager, "_handle_turn") as mock_handle:
        mock_handle.side_effect = [False, True]

        manager.game_loop()

        assert mock_handle.call_count == 2

        calls = mock_handle.call_args_list
        assert calls[0].args[0] == manager.player1
        assert calls[1].args[0] == manager.player2
