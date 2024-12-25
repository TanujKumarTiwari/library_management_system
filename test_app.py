import unittest
from app import app, db
from models import Book, Member

class LibraryManagementSystemTest(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        with app.app_context():
            db.create_all()
    
    def tearDown(self):
        with app.app_context():
            db.drop_all()

    def test_add_book(self):
        response = self.app.post('/books', json={'title': 'Test Book', 'author': 'Test Author', 'year': 2024})
        self.assertEqual(response.status_code, 201)
        self.assertIn('Book added successfully', response.json['message'])

    def test_get_books(self):
        self.app.post('/books', json={'title': 'Test Book', 'author': 'Test Author', 'year': 2024})
        response = self.app.get('/books')
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.json['books']), 0)

    def test_add_member(self):
        response = self.app.post('/members', json={'name': 'Test Member', 'email': 'test@example.com'})
        self.assertEqual(response.status_code, 201)
        self.assertIn('Member added successfully', response.json['message'])

if __name__ == '__main__':
    unittest.main()

