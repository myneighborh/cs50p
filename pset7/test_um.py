from um import count


def test_um():
    assert count("um") == 1
    assert count("um?") == 1


def test_upper_um():
    assert count("Um, thanks um...") == 2


def test_contain_um():
    assert count("Um, thanks for the album.") == 1
    assert count("Jump") == 0
    assert count("Um.... Let's Jump! um") == 2
