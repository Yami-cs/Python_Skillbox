import unittest
from mod2.finance import app

class TestFinancialApp(unittest.TestCase):
    def setUp(self):
        # Initialize test data for storage
        app.testing = True
        self.app = app.test_client()
        self.app.get("/add/20220101/50")
        self.app.get("/add/20220102/30")
        self.app.get("/add/20230101/20")
        self.app.get("/add/20230201/40")

    def test_add_expense(self):
        # Test adding an expense for a new date
        response = self.app.get("/add/20230101/50")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Expense of 50 rubles added for 1.1.2023", response.data)

        # Test adding an expense for an existing date
        response = self.app.get("/add/20230101/70")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Expense of 70 rubles added for 1.1.2023", response.data)

    def test_calculate_year(self):
        # Test calculating total expenses for 2022
        response = self.app.get("/calculate/2022")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Total expenses for 2022: 80 rubles", response.data)

        # Test calculating total expenses for 2023
        response = self.app.get("/calculate/2023")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Total expenses for 2023: 60 rubles", response.data)

        # Test calculating total expenses for a non-existing year
        response = self.app.get("/calculate/2024")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Total expenses for 2024: 0 rubles", response.data)

    def test_calculate_month(self):
        # Test calculating expenses for January 2023
        response = self.app.get("/calculate/2023/1")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Expenses for 1.2023: 20 rubles", response.data)

        # Test calculating expenses for February 2023
        response = self.app.get("/calculate/2023/2")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Expenses for 2.2023: 40 rubles", response.data)

        # Test calculating expenses for a non-existing month
        response = self.app.get("/calculate/2023/3")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Expenses for 3.2023: 0 rubles", response.data)

    def test_invalid_date_format(self):
        # Test adding an expense with invalid date format
        response = self.app.get("/add/2023-01-01/50")
        self.assertEqual(response.status_code, 404)

    def test_empty_storage(self):
        # Clear storage
        app.storage = {}

        # Test calculating total expenses for a non-existing year
        response = self.app.get("/calculate/2024")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Total expenses for 2024: 0 rubles", response.data)

if __name__ == "__main__":
    unittest.main()
