# Task Manager API
A RESTful API built with Django and Django REST Framework.

## Features
- CRUD operations for Tasks.
- Token-based Authentication.
- Search and Filtering (Search by title, Filter by status).
- User-specific data (Users only see their own tasks).

## Setup
1. Clone the repo.
2. Create a virtual environment: `python -m venv env`
3. Install dependencies: `pip install -r requirements.txt`
4. Migrate: `python manage.py migrate`
5. Run: `python manage.py runserver`