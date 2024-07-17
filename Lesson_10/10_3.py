
# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize("a, b, result", [
    (4, 2, 2),
    (3.5, 2, 1.75),
    pytest.param(-10, 5, -2, marks=pytest.mark.skip("какой-то косяк")),
    pytest.param(10, 0, ZeroDivisionError, marks=pytest.mark.zero_division)
], ids=["positive", "positive_float", "negative", "zero_division"])


def test_all_division(a, b, result):
    if result == ZeroDivisionError:
        with pytest.raises(ZeroDivisionError):
            all_division(a, b)
    else:
        assert all_division(a, b) == result
