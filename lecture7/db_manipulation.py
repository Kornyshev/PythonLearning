# Create a new database named "films_db".
# Use the SQLAlchemy library to create the database and tables in Python.
# Part 1: Setting up the Database
# Create one table for films, with the following columns:
#     films table:
#         id (integer, primary key)
#         title (string)
#         director (string)
#         release year (integer)
# Part 2: Manipulating with Database
#     Create script that:
#         Add 3 film to the film table.
#         Update 1 film
#         Print data from table
#         Delete all data from table
from typing import Iterable

from sqlalchemy import *
from sqlalchemy.orm import *

from create_db import Film


def print_all_films():
    session_maker = sessionmaker(bind=create_engine('sqlite:///films_db.db'))
    session = session_maker()
    all_films = session.query(Film).all()
    if len(all_films) == 0:
        print("\nTable 'films' is empty")
    else:
        print("\nAll films in the table:")
        for elem in session.query(Film).all():
            print(elem)


def clear_films_table():
    session_maker = sessionmaker(bind=create_engine('sqlite:///films_db.db'))
    session = session_maker()
    session.query(Film).delete()
    session.commit()


def add_films_to_db(films: Iterable[Film]):
    session_maker = sessionmaker(bind=create_engine('sqlite:///films_db.db'))
    session = session_maker()
    for film in films:
        session.add(film)
    session.commit()


def update_film_year_by_title(title: str, year: int):
    session_maker = sessionmaker(bind=create_engine('sqlite:///films_db.db'))
    session = session_maker()
    session.query(Film).filter(Film.title == title).update({'release_year': year})
    session.commit()


if __name__ == '__main__':
    print_all_films()
    films_list = [
        Film(title='The Shawshank Redemption', director='Frank Darabont', release_year=1994),
        Film(title='The Godfather', director='Francis Ford Coppola', release_year=1972),
        Film(title='The Dark Knight', director='Christopher Nolan', release_year=2022),  # Correct year: 2008
        Film(title='Forrest Gump', director='Robert Zemeckis', release_year=1994),
        Film(title='Inception', director='Christopher Nolan', release_year=2010),
        Film(title='The Matrix', director='The Wachowski Brothers', release_year=1999),
    ]
    add_films_to_db(films_list)
    print_all_films()
    update_film_year_by_title('The Dark Knight', 2008)
    print_all_films()
    clear_films_table()
    print_all_films()
