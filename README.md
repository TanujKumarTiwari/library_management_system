# Library Management System API

## Description
This is a Flask-based Library Management System API that supports CRUD operations for books and members, search functionality for books by title/author, pagination for books, and token-based authentication.

## Features
- Add, update, delete, and get details of books and members.
- Search books by title or author.
- Pagination for listing books.
- Token-based authentication for secured endpoints.

## How to Run the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repository/library-management-system.git
   cd library-management-system
2. Set up a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
4. Install dependencies:
   ```bash
   pip install flask
   pip install flask_sqlalchemy
5. Run the application:
   ```bash
   python app.py
6. The API will be available at http://127.0.0.1:5000/.
