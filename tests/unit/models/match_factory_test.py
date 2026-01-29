from src.models.match_factory import MatchFactory
from src.models.board import Board
from src.models.player import Player
from src.models.player_strategies import HumanStrategy, RandomBotStrategy

def test_setup_classic_pvp():
    
    board, players = MatchFactory.setup_classic_pvp()
    assert type(board) is Board

    assert len(players) == 2
    assert type(players[0]) is Player
    assert type(players[0].move_strategy) is HumanStrategy
    assert type(players[1]) is Player
    assert type(players[1].move_strategy) is HumanStrategy

def test_setup_classic_random_vs_random():
    
    board, players = MatchFactory.setup_classic_random_vs_random()
    assert type(board) is Board

    assert len(players) == 2
    assert type(players[0]) is Player
    assert type(players[0].move_strategy) is RandomBotStrategy
    assert type(players[1]) is Player
    assert type(players[1].move_strategy) is RandomBotStrategy

