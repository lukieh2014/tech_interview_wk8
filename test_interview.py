import pytest
from unittest.mock import patch, MagicMock
from interview import get_score_for_word, give_seven_tiles, generate_player_rack

def test_gets_correct_score():
    score = get_score_for_word("GUARDIAN")

    assert score == 10

def test_invalid_word():
    with pytest.raises(TypeError):
        get_score_for_word(123)

def test_empty_word():
    assert get_score_for_word("") == 0

def test_gets_seven_tiles():
    player_hand = give_seven_tiles()

    assert len(player_hand) == 7


def test_gen_player_rack():
    player_hand = generate_player_rack()

    assert len(player_hand) == 7