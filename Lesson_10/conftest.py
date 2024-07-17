import pytest
import datetime


@pytest.fixture(scope='session', autouse=True)
def start_time(request):
    print('\nStart time:', datetime.datetime.now())


@pytest.fixture()
def test_time(request):
    start = datetime.datetime.now()
    yield
    total_time = datetime.datetime.now() - start
    print(f'Test duration: {total_time.seconds}s {total_time.microseconds}µs')


@pytest.fixture()
def setup_fixture():
    pass
    yield
    pass

