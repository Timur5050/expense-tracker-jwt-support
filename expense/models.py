from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float
from sqlalchemy.orm import relationship

from database import Base


class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String)
    amount = Column(Float)
    date = Column(Date)
    user_id = Column(Integer, ForeignKey("users.id"))
