from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# my_engine = create_engine("sqlite:///FastApi.db", connect_args={'check_same_thread': False})
my_engine = create_engine("postgresql+psycopg2://postgres:123456789@localhost:5432/monitoring")

my_base = declarative_base()

session_local = sessionmaker(bind=my_engine, autoflush=False, autocommit=False)


def get_db():
    session = session_local()

    try:
        yield session
    finally:
        session.close()
