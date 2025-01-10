from decorators import log

@log(filename="")
def numbers_sum(x: int, y: int) -> int:
    return x + y


def test_log():
    result = numbers_sum(6, 12)
    assert result == 18


def test_log_different_argtypes(capsys):
    numbers_sum("one", 2)
    output = capsys.readouterr()
    assert output.out == "numbers_sum error: TypeError. Inputs: ('one', 2), {}\n\n"


def test_with_more_args(capsys):
    numbers_sum(1, 2, 3)
    output = capsys.readouterr()
    assert output.out == "numbers_sum error: TypeError. Inputs: (1, 2, 3), {}\n\n"
