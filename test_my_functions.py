import pytest
from tested_func import get_list
from tested_func import ending
from tested_func import find_missing_number

# ==================
# 1. тестируем get_list
# ==================
# список данных для теста
list_example = [(3, 6.62), (5, 11.55), (8, 19.19)]


@pytest.mark.parametrize('a, expected_result', list_example)
def test_get_list_good(a, expected_result):
    assert get_list(a) == expected_result


# данные для проверки ошибок
list_errors = [(TypeError, '2'), (ZeroDivisionError, 0)]


@pytest.mark.parametrize('expected_exception, x', list_errors)
def test_get_list_with_error(expected_exception, x):
    with pytest.raises((expected_exception)):
        get_list(x)


# ==================
# 2. тестируем ending
# ==================
# список данных для теста
list_example = [(0, 'конфет'), (1, 'конфета'), (3, 'конфеты'), (5, 'конфет')]


@pytest.mark.parametrize('a, expected_result', list_example)
def test_get_list_good(a, expected_result):
    assert ending(a) == expected_result


# данные для проверки ошибок
list_errors = [(TypeError, '2')]


@pytest.mark.parametrize('expected_exception, x', list_errors)
def test_get_list_with_error(expected_exception, x):
    with pytest.raises((expected_exception)):
        ending(x)


# ==================
# 3. тестируем find_missing_number
# ==================
# список данных для теста
list_example = [([1, 2, 4], 3), ([3, 4, 5, 7], 6), ([6, 7, 8, 10], 9), ([1, 2, 3], None)]


@pytest.mark.parametrize('a, expected_result', list_example)
def test_get_list_good(a, expected_result):
    assert find_missing_number(a) == expected_result


# данные для проверки ошибок
list_errors = [(TypeError, 0)]


@pytest.mark.parametrize('expected_exception, x', list_errors)
def test_get_list_with_error(expected_exception, x):
    with pytest.raises((expected_exception)):
        find_missing_number(x)

# декоратор python
# @pytest.mark.parametrize('a, b, expected_result', [(10, 2, 5),
#                                                    (10, 5, 2),
#                                                    (12, 3, 4),
#                                                    (10, 10, 1),
#                                                    (10, -5, -2),
#                                                    (5, 2, 2.5)])
# def test_division_good(a, b, expected_result):
#     assert division(a, b) == expected_result
# Оператор assert – это встроенный оператор или ключевое слово в Python, используемое для отладки кода.
# Это своего рода проверка, которая исследует функциональность вашего кода.
# Оператор assert работает как логическое выражение, проверяя, является ли заданное условие истинным
# или ложным. Если условие истинно, то ничего не происходит и выполняется следующая строка кода.
# Если же условие ложно, оператор assert останавливает выполнение программы и выдает ошибку.
# В этом случае assert работает как ключевое слово raise и выводит исключение.
# Исключение, вызванное оператором assert, также называется AssertionError.
# Синтаксис assert <condition>, <message>, например, assert num2 != 0, "The divisor is zero"
