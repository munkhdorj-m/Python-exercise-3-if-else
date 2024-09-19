import pytest
from assignment import find_lesser_of_two_numbers, sum_of_numbers_not_divisible_by_11, find_largest_digit_of_3_digit_number, check_number_greater_than_10, convert_number_to_letter_rating

@pytest.mark.parametrize("num1, num2, expected", [
    (5, 10, 5),
    (15, 5, 5),
    (7, 7, 7),
    (100, 99, 99)
])
def test1(num1, num2, expected):
    assert find_lesser_of_two_numbers(num1, num2) == expected

@pytest.mark.parametrize("num1,num2,num3,num4,expected", [
    (11, 22, 33, 44, 0),
    (1, 2, 3, 4, 10),
    (10, 20, 30, 40, 100),
    (11, 12, 13, 14, 39)
])
def test2(num1,num2,num3,num4, expected):
    assert sum_of_numbers_not_divisible_by_11(num1,num2,num3,num4) == expected

@pytest.mark.parametrize("number, expected", [
    (123, 3),
    (456, 6),
    (789, 9),
    (321, 3)
])
def test3(number, expected):
    assert find_largest_digit_of_3_digit_number(number) == expected

@pytest.mark.parametrize("number, expected_output", [
    (5, "no"),
    (10, "no"),
    (11, "yes"),
    (20, "yes")
])
def test4(capsys, number, expected_output):
    assert check_number_greater_than_10(number).strip().lower() == expected_output

@pytest.mark.parametrize("number, expected", [
    (95, 'a'),
    (85, 'b'),
    (75, 'c'),
    (65, 'd'),
    (50, 'f'),
    (101, 'error'),
    (-5, 'error')
])
def test5(number, expected):
    assert convert_number_to_letter_rating(number).strip().lower() == expected
