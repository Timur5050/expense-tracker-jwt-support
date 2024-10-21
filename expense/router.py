from datetime import datetime

from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from dependenies import get_db
from expense.schemas import ExpensesListSchema, ExpenseSchema
from expense import crud
from auth.middleware import get_user_id

router = APIRouter(prefix="/expenses", tags=["expenses"])


@router.get("/", response_model=list[ExpensesListSchema])
def get_expenses(request: Request, db: Session = Depends(get_db)):
    user_id = get_user_id(request)

    return crud.get_all_expenses(
        db=db,
        user_id=user_id
    )


@router.post("/", response_model=ExpensesListSchema)
def create_expense(request: Request, expense: ExpenseSchema, db: Session = Depends(get_db)):
    user_id = get_user_id(request)

    return crud.create_expense(
        db=db,
        expense=expense,
        user_id=user_id
    )


@router.delete("/{pk}/", response_model=ExpensesListSchema)
def delete_expense(request: Request, pk: int, db: Session = Depends(get_db)):
    user_id = get_user_id(request)

    return crud.delete_expense(
        db=db,
        expense_id=pk,
        user_id=user_id
    )


@router.get("/summary/")
def get_expense_summary(request: Request, db: Session = Depends(get_db)):
    user_id = get_user_id(request)

    return crud.get_summary(
        db=db,
        user_id=user_id
    )


@router.get("/summary/{month}/")
def get_expense_during_month(
        request: Request,
        month: int,
        db: Session = Depends(get_db)
):
    user_id = get_user_id(request)

    return crud.get_summary_during_month(
        db=db,
        month_number=month,
        user_id=user_id
    )


@router.get("/summary/stats/last_week/")
def get_expense_last_week(
        request: Request,
        db: Session = Depends(get_db)
):
    user_id = get_user_id(request)

    return crud.get_summary_per_past_week(
        db=db,
        user_id=user_id
    )


@router.get("/summary/stats/last_month/")
def get_expense_last_month(
        request: Request,
        db: Session = Depends(get_db)
):
    user_id = get_user_id(request)

    return crud.get_summary_per_past_month(
        db=db,
        user_id=user_id
    )


@router.get("/summary/stats/{start_date}/{end_date}/")
def get_expense_stats_per_custom_date(
        request: Request,
        start_date: datetime,
        end_date: datetime,
        db: Session = Depends(get_db)
):
    user_id = get_user_id(request)

    return crud.get_summary_per_custom_data(
        db=db,
        user_id=user_id,
        start_date=start_date,
        end_date=end_date
    )
