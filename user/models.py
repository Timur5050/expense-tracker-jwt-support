from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)
    date_joined = Column(DateTime, default=datetime.now)
    last_login = Column(DateTime, default=datetime.now)
