import pytest

from main import BooksCollector


@pytest.fixture(scope='session')
def test_book_collector():
    collector = BooksCollector()

    return collector