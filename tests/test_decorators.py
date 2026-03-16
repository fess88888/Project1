import pytest
import os
from src.decorators import log


@log()
def divide_function(x: float, y: float) -> float:
    return x / y


@pytest.mark.parametrize("x, y, expected_output", [
    (3, 2, "Function: divide_function ok. Result: 1.5\n"),
    (1, 0, "Function: divide_function error: ZeroDivisionError. Inputs: (1, 0), {}\n")
])
def test_log_to_console(capsys, x: float, y: float, expected_output: str) -> None:
    if y == 0:
        with pytest.raises(ZeroDivisionError):
            divide_function(x, y)
    else:
        divide_function(x, y)

    captured = capsys.readouterr()
    assert captured.out == expected_output


@log(filename="mylog.txt")
def square_divided_by_number(x: float, y: float) -> float:
    return x * x / y


@pytest.mark.parametrize("x, y, expected_output", [
    (6, 2, "Function: square_divided_by_number ok. Result: 18.0\n"),
    (1, 0, "Function: square_divided_by_number error: ZeroDivisionError. Inputs: (1, 0), {}\n")
])
def test_log_to_file(x: float, y: float, expected_output: str) -> None:

    log_file = "mylog.txt"
    if os.path.exists(log_file):
        os.remove(log_file)

    if y == 0:
        with pytest.raises(ZeroDivisionError):
            square_divided_by_number(x, y)
    else:
        square_divided_by_number(x, y)

    with open(log_file, "r", encoding="utf-8") as file:
        logs = file.read()
        assert expected_output in logs

    if os.path.exists(log_file):
        os.remove(log_file)
