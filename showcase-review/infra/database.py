from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:123456@localhost:5432/postgres'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

Sessionmaker = sessionmaker()


Base = declarative_base()


def get_db():
    db = Sessionmaker()

    try:
        yield db
    except:
        db.close()