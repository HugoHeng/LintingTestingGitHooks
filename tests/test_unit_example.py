from app import even_or_odd


def test_even_or_odd():
    assert even_or_odd(2) == 1
    assert even_or_odd(3) == 0
# Test function