from typing import Type
from datetime import datetime, timedelta

from fastapi import HTTPException, status
from sqlalchemy import func
from sqlalchemy.orm import Session

from expense.models import Expense
from expense.schemas import ExpenseSchema
from user.models import User


def get_all_expenses(db: Session, user_id: int) -> list[Type[Expense]]:
    return db.query(Expense).filter(Expense.user_id == user_id).all()


def create_expense(db: Session, expense: ExpenseSchema, user_id: int) -> Expense:
    expense = Expense(
        description=expense.description,
        amount=expense.amount,
        user_id=user_id,
        date=datetime.now()
    )
    db.add(expense)
    db.commit()
    db.refresh(expense)
    return expense


def delete_expense(db: Session, expense_id: int, user_id: int) -> None:
    expense = db.query(Expense).filter(Expense.id == expense_id).first()
    if expense is None or expense.user_id != user_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    db.delete(expense)
    db.commit()
    return expense


def get_summary(db: Session, user_id: int) -> float:
    user_expenses = db.query(Expense).filter(Expense.user_id == user_id).all()
    return sum(expense.amount for expense in user_expenses)


def get_summary_during_month(db: Session, month_number: int, user_id: int) -> float:
    user_expenses = db.query(Expense).filter(
        Expense.user_id == user_id,
        func.extract('month', Expense.date) == month_number
    ).all()
    return sum(expense.amount for expense in user_expenses)


def get_summary_per_past_week(db: Session, user_id: int) -> list[Type[Expense]]:
    today = datetime.now().date()
    week_ago = today - timedelta(days=7)

    user_expenses = db.query(Expense).filter(
        Expense.user_id == user_id,
        Expense.date.between(week_ago, today)
    ).all()

    return user_expenses


def get_summary_per_past_month(db: Session, user_id: int) -> list[Type[Expense]]:
    today = datetime.now().date()
    first_day_of_month = today.replace(day=1)
    previous_month_last_day = first_day_of_month - timedelta(days=1)
    previous_month_first_day = previous_month_last_day.replace(day=1)

    user_expenses = db.query(Expense).filter(
        Expense.user_id == user_id,
        Expense.date.between(previous_month_first_day, previous_month_last_day)
    ).all()

    return user_expenses


def get_summary_per_custom_data(
        db: Session,
        user_id: int,
        start_date: datetime,
        end_date: datetime
) -> list[Type[Expense]]:
    user_expenses = db.query(Expense).filter(
        Expense.user_id == user_id,
        Expense.date.between(start_date, end_date)
    ).all()

    return user_expenses
