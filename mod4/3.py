import unittest
from Registration import app, RegistrationForm

class TestRegistrationForm(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_valid_registration(self):
        # Test valid registration data
        response = self.app.post("/reg", data={
            "email": "test@example.com",
            "phone": "1234567890",
            "name": "John Doe",
            "address": "123 Main St",
            "index": 12345,
            "comment": "Test comment"
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn("Successfuly registered user", response.data.decode())

    def test_invalid_email(self):
        # Test invalid email format
        response = self.app.post("/reg", data={
            "email": "invalid_email",
            "phone": "1234567890",
            "name": "John Doe",
            "address": "123 Main St",
            "index": 12345,
            "comment": "Test comment"
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn("Invalid input", response.data.decode())

    def test_invalid_phone(self):
        # Test invalid phone format (less than 10 digits)
        response = self.app.post("/reg", data={
            "email": "test@example.com",
            "phone": "123456789",
            "name": "John Doe",
            "address": "123 Main St",
            "index": 12345,
            "comment": "Test comment"
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn("Invalid input", response.data.decode())

    def test_invalid_name(self):
        # Test empty name field
        response = self.app.post("/reg", data={
            "email": "test@example.com",
            "phone": "1234567890",
            "name": "",
            "address": "123 Main St",
            "index": 12345,
            "comment": "Test comment"
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn("Invalid input", response.data.decode())

    def test_invalid_index(self):
        # Test invalid index format (not an integer)
        response = self.app.post("/reg", data={
            "email": "test@example.com",
            "phone": "1234567890",
            "name": "John Doe",
            "address": "123 Main St",
            "index": "invalid_index",
            "comment": "Test comment"
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn("Invalid input", response.data.decode())

if __name__ == "__main__":
    unittest.main()
