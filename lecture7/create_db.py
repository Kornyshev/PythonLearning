from sqlalchemy import *
from sqlalchemy.orm import *

Base = declarative_base()


class Film(Base):
    __tablename__ = 'films'

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    director = Column(String(255))
    release_year = Column(Integer)

    def __str__(self):
        return f"Title: {self.title}, director: {self.director}, year: {self.release_year}"


if __name__ == '__main__':
    Base.metadata.create_all(create_engine('sqlite:///films_db.db'))
