import pytest

from hw2 import *


@pytest.fixture
def prepared_db():
    db_name = 'example.sqlite'
    table_name = 'books'
    list_of_books = [('Farenheit 451', 'Bradbury'), ('Brave New World', 'Huxley'), ('1984', 'Orwell')]
    return db_name, table_name, list_of_books


def test_db_as_collection(prepared_db):
    db_name, table_name, list_of_books = prepared_db
    books = TableData(database_name=db_name, table_name=table_name)
    assert len(books) == 3
    assert [book for book in books] == list_of_books
    assert 'Yeltsin' not in books
