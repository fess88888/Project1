import pytest
from src.generators import card_number_generator


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (1, 4, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003", "0000 0000 0000 0004"]),
        (7777777777777777, 7777777777777778, ["7777 7777 7777 7777", "7777 7777 7777 7778"]),
        (4444, 4444, ["0000 0000 0000 4444"]),
    ],
)
def test_card_number_generator(start: int, stop: int, expected: str) -> None:
    result = list(card_number_generator(start, stop))
    assert result == expected


def test_card_number_generator_incorrect_range() -> None:
    with pytest.raises(ValueError) as exc_info:
        list(card_number_generator(2, 222222222222222222222222222))
    assert str(exc_info.value) == "Введенные параметры не входят в диапазон"
