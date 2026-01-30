import pytest

from connect4.views.cli_view import CLIView
from connect4.models.board import Cell


def test_view_initialization_fails_with_missing_config():
    incomplete_config = {Cell.PLAYER1.value: {"COLOR": "red", "SHAPE": "X"}}

    with pytest.raises(AttributeError) as excinfo:
        CLIView(player_config=incomplete_config)

    assert f"Missing configuration for player {Cell.PLAYER2}" in str(excinfo.value)


def test_get_player_ansi_color(view):
    red_code = view._get_player_ansi_color(Cell.PLAYER1.value)
    assert red_code == "\033[31m"

    assert view._get_player_ansi_color(Cell.EMPTY.value) == ""


def test_convert_cell_data_to_player_config(view):
    assert view._convert_cell_data_to_player_config(Cell.EMPTY.value) == "   "

    rendered_x = view._convert_cell_data_to_player_config(Cell.PLAYER1.value)
    assert "X" in rendered_x
    assert "\033[31m" in rendered_x

    rendered_bg = view._convert_cell_data_to_player_config(Cell.PLAYER2.value)
    assert "X" not in rendered_bg
    assert "\033[43m" in rendered_bg


def test_print_board_layout(view, capsys):
    board_state = [
        [Cell.PLAYER1.value, Cell.EMPTY.value],
        [Cell.PLAYER2.value, Cell.EMPTY.value],
    ]

    view.print_board(board_state)
    captured = capsys.readouterr().out

    assert "0   1" in captured
    assert "|" in captured


def test_get_user_input_valid(view, monkeypatch):
    # monkeypatch simulates user typing "3" then pressing Enter
    monkeypatch.setattr("builtins.input", lambda _: "3")
    assert view.get_user_input("Alice") == 3


def test_get_user_input_invalid(view, monkeypatch):
    # monkeypatch simulates user typing "abc"
    monkeypatch.setattr("builtins.input", lambda _: "abc")
    assert view.get_user_input("Alice") == -1


def test_print_error_message(view, capsys):
    view.print_error_message("Logic Error")

    captured = capsys.readouterr().out
    assert "Logic Error" in captured
    assert "\033[31m" in captured
    assert "\033[0m" in captured


def test_print_game_over_message(view, capsys):
    view.print_game_over_screen("Game Over")

    captured = capsys.readouterr().out
    assert "Game Over" in captured
    assert "\033[31m" not in captured
    assert "\033[33m" not in captured
    assert "\033[0m" in captured

    view.print_game_over_screen("Game Over", player_id=Cell.PLAYER1.value)

    captured = capsys.readouterr().out
    assert "Game Over" in captured
    assert "\033[31m" in captured
    assert "\033[0m" in captured
