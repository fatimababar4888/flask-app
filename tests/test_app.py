import unittest
from app import app

class FlaskAppTestCase(unittest.TestCase):
    
    def setUp(self):
        """Set up test client"""
        self.app = app.test_client()
        self.app.testing = True
    
    def test_index_route(self):
        """Test home page route"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_about_route(self):
        """Test about page route"""
        response = self.app.get('/about')
        self.assertEqual(response.status_code, 200)
    
    def test_contact_get(self):
        """Test contact page GET request"""
        response = self.app.get('/contact')
        self.assertEqual(response.status_code, 200)
    
    def test_contact_post_success(self):
        """Test contact form submission with valid data"""
        response = self.app.post('/contact', data={
            'name': 'Test User',
            'email': 'test@example.com',
            'message': 'Test message'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
    def test_contact_post_missing_fields(self):
        """Test contact form submission with missing fields"""
        response = self.app.post('/contact', data={
            'name': 'Test User',
            'email': '',
            'message': ''
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()

