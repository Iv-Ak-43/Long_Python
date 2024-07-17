
# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

"""import pytest
from test_10_2 import all_division


class TestClass:

    @pytest.mark.usefixtures('start_time')
    @pytest.mark.parametrize('args, result', [pytest.param([15], 15, marks=pytest.mark.smoke),
                                              pytest.param([2, 8], 0.25)])
    def test1(self, args, result):
        assert all_division(*args) == result

    @pytest.mark.usefixtures('run_time')
    @pytest.mark.parametrize('args, result', [pytest.param([56, 2, 7, 4], 1.0),
                                              pytest.param([4, 2], 0, marks=pytest.mark.skip('плохой test!!'))])
    def test2(self, args, result):
        assert all_division(*args) == result"""

import pytest

@pytest.mark.usefixtures("setup_fixture")
class TestClass:
    def test_one(self, test_time):
        assert 1 == 1
    def test_two(self):
        assert 2 == 2
    def test_three(test_time):
        assert 3 == 3
    def test_four(setup_fixture, test_time):
        assert 4 == 4

