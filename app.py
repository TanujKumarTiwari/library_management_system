from flask import Flask, request, jsonify
from models import db, Book, Member
from auth import token_required
from utils import paginate, search_books

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
db.init_app(app)

@app.route('/books', methods=['POST'])
@token_required
def add_book():
    data = request.get_json()
    title = data.get('title')
    author = data.get('author')
    year = data.get('year')

    if not title or not author:
        return jsonify({'message': 'Title and author are required'}), 400

    new_book = Book(title=title, author=author, year=year)
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'message': 'Book added successfully', 'book': new_book.to_dict()}), 201

@app.route('/books', methods=['GET'])
@token_required
def get_books():
    page = request.args.get('page', 1, type=int)
    search_query = request.args.get('search', '')
    books = search_books(search_query)
    books_paginated = paginate(books, page)

    return jsonify({
        'books': [book.to_dict() for book in books_paginated.items],
        'total': books_paginated.total,
        'pages': books_paginated.pages,
        'current_page': books_paginated.page
    })

@app.route('/book/<int:id>', methods=['GET'])
@token_required
def get_book(id):
    book = Book.query.get_or_404(id)
    return jsonify(book.to_dict())

@app.route('/book/<int:id>', methods=['PUT'])
@token_required
def update_book(id):
    data = request.get_json()
    book = Book.query.get_or_404(id)

    book.title = data.get('title', book.title)
    book.author = data.get('author', book.author)
    book.year = data.get('year', book.year)

    db.session.commit()
    return jsonify({'message': 'Book updated', 'book': book.to_dict()})

@app.route('/book/<int:id>', methods=['DELETE'])
@token_required
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': 'Book deleted successfully'})

@app.route('/members', methods=['POST'])
@token_required
def add_member():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    if not name or not email:
        return jsonify({'message': 'Name and email are required'}), 400

    new_member = Member(name=name, email=email)
    db.session.add(new_member)
    db.session.commit()
    return jsonify({'message': 'Member added successfully', 'member': new_member.to_dict()}), 201

@app.route('/members', methods=['GET'])
@token_required
def get_members():
    members = Member.query.all()
    return jsonify([member.to_dict() for member in members])

@app.route('/member/<int:id>', methods=['GET'])
@token_required
def get_member(id):
    member = Member.query.get_or_404(id)
    return jsonify(member.to_dict())

@app.route('/member/<int:id>', methods=['PUT'])
@token_required
def update_member(id):
    data = request.get_json()
    member = Member.query.get_or_404(id)

    member.name = data.get('name', member.name)
    member.email = data.get('email', member.email)

    db.session.commit()
    return jsonify({'message': 'Member updated', 'member': member.to_dict()})

@app.route('/member/<int:id>', methods=['DELETE'])
@token_required
def delete_member(id):
    member = Member.query.get_or_404(id)
    db.session.delete(member)
    db.session.commit()
    return jsonify({'message': 'Member deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
