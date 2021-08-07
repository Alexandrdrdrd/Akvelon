from main import NumberFormatter

my_object = NumberFormatter()
def test_empty_string():
    assert my_object.parseInt("") == "Empty string is not applicable"


def test_only_digits():
    assert my_object.parseInt("1234") == int(1234)


def test_plus_before_numeric_value():
    assert my_object.parseInt("+1234") == 1234


def test_minus_before_numeric_value():
    assert my_object.parseInt("-1234") == -1234


def test_the_string_is_shorter_than_two_characters():
    assert my_object.parseInt("1") == "Incorrect line length"


def test_symbol_before_digit():
    assert my_object.parseInt("*1234") == "Invalid input format"


def test_character_after_digits():
    assert my_object.parseInt("1234*") == "Invalid input format"


def test_character_between_digits():
    assert my_object.parseInt("12*34") == "Invalid input format"
