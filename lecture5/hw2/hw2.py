import sqlite3


class TableData:
    def __init__(self, database_name, table_name):
        self._database_name = database_name
        self._table_name = table_name

    def __len__(self):
        with sqlite3.connect(self._database_name) as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT COUNT(*) FROM {self._table_name}")
            return cursor.fetchone()[0]

    def __getitem__(self, author):
        with sqlite3.connect(self._database_name) as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {self._table_name} WHERE author=?", (author,))
            data = cursor.fetchone()
            if data is None:
                raise KeyError(f"No book found with author {author}")
            return data

    def __contains__(self, author):
        with sqlite3.connect(self._database_name) as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT COUNT(*) FROM {self._table_name} WHERE author=?", (author,))
            return cursor.fetchone()[0] > 0

    def __iter__(self):
        with sqlite3.connect(self._database_name) as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {self._table_name} ORDER BY author")
            while True:
                data = cursor.fetchone()
                if data is None:
                    break
                yield data


if __name__ == '__main__':
    books = TableData(database_name='example.sqlite', table_name='books')
    print(books['Bradbury'])
    print(len(books))
    for book in books:
        print(f"Type: {type(book)}. Instance: {book}")
    print('Yeltsin' in books)
    print('Bradbury' in books)
