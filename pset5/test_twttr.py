from twttr import shorten


def test_lowercase_vowels():
    assert shorten("education") == "dctn"


def test_uppercase_vowels():
    assert shorten("EDUCATION") == "DCTN"


def test_mixed_case():
    assert shorten("HeLLo") == "HLL"


def test_with_numbers():
    assert shorten("a1e2i3o4u") == "1234"


def test_with_special_characters():
    assert shorten("h@ck!ng") == "h@ck!ng"


def test_empty_string():
    assert shorten("") == ""


def test_only_vowels():
    assert shorten("aeiouAEIOU") == ""


def test_with_spaces():
    assert shorten("hi there") == "h thr"


def test_original_example():
    assert shorten("Twitter") == "Twttr"
