## Project Description

This application allows users to manage their expenses and view summaries through a REST API. The application includes user authentication and token-based access control (JWT). Users can register, log in, and manage their expenses, which are stored in a database. The project also provides functionality for viewing total expenses, filtering by month, and refreshing authentication tokens.

project idea: https://roadmap.sh/projects/expense-tracker-api

## Main Features
1. Expense Management (CRUD Operations)
    - Add Expense: Users can create a new expense by providing a description and amount.
    - Update Expense: Existing expenses can be updated.
    - Delete Expense: Users can delete an expense by its unique ID.
    - List Expenses: Users can view a list of all their expenses.
    - View Summary: Users can get a summary of their total expenses.
    - Monthly Summary: Users can view a summary of expenses for a specific month.

2. User Authentication and JWT
   -  User Registration: New users can register by providing a username and password.
   -  User Login: Users can log in with their credentials, receiving access and refresh tokens.
   -  Token Refresh: Users can refresh their access tokens using a valid refresh token.

## Tecknologies used
  - FastAPI: For creating the RESTful API endpoints.
  - SQLAlchemy: For interacting with the database.
  - JWT (JSON Web Tokens): For token-based authentication and user session management.
  - SQLite/PostgreSQL (or any database): Used for storing user and expense data.
  - Pydantic: For request validation and response models.
  - Python: The core language for building the backend services.



## how to run
```sh
# Clone the repository
git clone https://github.com/Timur5050/expense-tracker-jwt-support.git
# Change to the project directory
cd expense-tracker-jwt-support
# Create a virtual environment
python -m venv venv
# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
# Install required packages
pip install -r requirements.txt
# create directory in project with files encoders(private and public keys): private.pem and public.pem
# run the server
python -m uvicorn main:app --port=8000 --reload
```
