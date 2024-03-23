import unittest
from flask import Flask
from flask_testing import TestCase
from mod5.execute import app

class TestExecuteCodeEndpoint(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_timeout_below_execution_time(self):
        # Test when timeout is lower than execution time
        code = "import time; time.sleep(10)"
        response = self.client.post('/execute_code', data={'code': code, 'timeout': 5})
        self.assertIn(b'Execution timed out', response.data)

    def test_invalid_form_data(self):
        # Test when invalid form data is provided
        response = self.client.post('/execute_code', data={})
        self.assertIn(b'error', response.data)

    def test_unsafe_code_input(self):
        # Test unsafe input (shell=True)
        code = "python -c \"print('Hello world!')\""
        response = self.client.post('/execute_code', data={'code': code, 'timeout': 10})
        self.assertIn(b'error', response.data)

    def test_valid_request(self):
        # Test valid request
        code = "print('Hello world!')"
        response = self.client.post('/execute_code', data={'code': code, 'timeout': 10})
        self.assertIn(b'Hello world!', response.data)

if __name__ == '__main__':
    unittest.main()
