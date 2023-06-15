from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from constants import SQL_CONNECTION_STRING

Base = declarative_base()
db_engine = create_engine(SQL_CONNECTION_STRING)
Session = sessionmaker()
Session.configure(bind = db_engine)
session = Session()