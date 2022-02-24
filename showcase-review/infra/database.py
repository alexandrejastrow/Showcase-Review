from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

uri = os.getenv("DATABASE_URL", "postgresql://postgres:123456@localhost:5432/postgres")
if uri and uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

engine = create_engine(
    "postgresql://fkyfkxfsvwqzxg:65d8f79ffb5fd13dd3b6afe5dfc3d1101c3a9fcadc2d53aab1d24ab5c5c933be@ec2-44-194-113-156.compute-1.amazonaws.com:5432/d1e9c4btsbkqn3"
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()

    try:
        yield db
    except:
        db.close()