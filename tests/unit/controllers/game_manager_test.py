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

    result = manager._handle_turn(manager.player1)

    assert result is True
    manager.game_board.add_piece.assert_called_once()
    manager.game_board.has_player_won.assert_called_once()
    manager.game_board.is_tie.assert_not_called()


def test_handle_turn_game_tied(manager):
    manager.game_board.is_column_playable.return_value = True
    manager.game_board.has_player_won.return_value = False
    manager.game_board.is_tie.return_value = True

    result = manager._handle_turn(manager.player1)

    assert result is True
    manager.game_board.add_piece.assert_called_once()
    manager.game_board.has_player_won.assert_called_once()
    manager.game_board.is_tie.assert_called_once()


def test_handle_turn_game_not_finished(manager):
    manager.game_board.is_column_playable.return_value = True
    manager.game_board.has_player_won.return_value = False
    manager.game_board.is_tie.return_value = False

    result = manager._handle_turn(manager.player1)

    assert result is False
    manager.game_board.add_piece.assert_called_once()
    manager.game_board.has_player_won.assert_called_once()
    manager.game_board.is_tie.assert_called_once()
