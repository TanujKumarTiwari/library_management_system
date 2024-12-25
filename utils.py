from flask_sqlalchemy import Pagination
from models import Book

def paginate(query, page, per_page=5):
    return query.paginate(page=page, per_page=per_page, error_out=False)

def search_books(query_string):
    if query_string:
        return Book.query.filter(Book.title.contains(query_string) | Book.author.contains(query_string)).all()
    return Book.query.all()
