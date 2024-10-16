from datetime import datetime

from pydantic import BaseModel


class ExpenseSchema(BaseModel):
    description: str
    amount: int


class ExpensesListSchema(ExpenseSchema):
    id: int
    date: datetime
    user_id: int
