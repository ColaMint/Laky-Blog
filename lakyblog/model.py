from lakyblog.setting import setting
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import Column, Integer, String
from flask.ext.login import UserMixin

engine = create_engine(setting['database']['url'])
db_session = scoped_session(sessionmaker(autocommit=True,
                                        autoflush=False,
                                        bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    # create database if not exists
    if not database_exists(engine.url):
        create_database(engine.url)

    # create tables if not exist
    Base.metadata.create_all(bind=engine)

class User(Base, UserMixin):
    __tablename__ = 'user'

    id       = Column(Integer, primary_key=True)
    username = Column(String(64), unique=True, nullable=False)
    password = Column(String(64), nullable=False)
    nickname = Column(String(64), nullable=False)
    email    = Column(String(64), nullable=False)

    def __init__(self, username, password, nickname, email):
        self.username = username
        self.password = password
        self.nickname = nickname
        self.email    = email

    def __repr__(self):
        return '<User: %s>' % self.username
