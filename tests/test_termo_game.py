import pytest
from termo_game import TermoGame

def test_correct_attempt():
    game = TermoGame("termo")
    feedback = game.check_word("termo")
    assert feedback == ['green', 'green', 'green', 'green', 'green']
    assert game.is_solved(feedback) == True

def test_incorrect_attempt():
    game = TermoGame("termo")
    feedback = game.check_word("abcdj")
    assert feedback == ['black', 'black', 'black', 'black', 'black']
    assert game.is_solved(feedback) == False

def test_partial_correct_attempt():
    game = TermoGame("termo")
    feedback = game.check_word("metro")
    assert feedback == ['yellow', 'green', 'yellow', 'yellow', 'green']
    assert game.is_solved(feedback) == False

def test_invalid_length_attempt():
    game = TermoGame("termo")
    with pytest.raises(ValueError):
        game.check_word("term")

def test_max_attempts():
    game = TermoGame("termo")
    for _ in range(6):
        game.check_word("abcde")
    assert game.can_attempt() == False

def test_before_max_attempts():
    game = TermoGame("termo")
    for _ in range(5):
        game.check_word("abcde")
    assert game.can_attempt() == True
