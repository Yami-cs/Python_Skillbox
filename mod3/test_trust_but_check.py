import unittest
import datetime

class Person:
    def __init__(self, name: str, year_of_birth: int, address: str = '') -> None:
        self.name: str = name
        self.yob: int = year_of_birth
        self.address: str = address

    def get_age(self) -> int:
        now: datetime.datetime = datetime.datetime.now()
        return now.year - self.yob

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    def set_address(self, address: str) -> None:
        self.address = address

    def get_address(self) -> str:
        return self.address

    def is_homeless(self) -> bool:
        return self.address == ''


class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person = Person('John Doe', 1990, '123 Street')

    def test_get_age(self):
        current_year = datetime.datetime.now().year
        self.assertEqual(self.person.get_age(), current_year - 1990)

    def test_get_name(self):
        self.assertEqual(self.person.get_name(), 'John Doe')

    def test_set_name(self):
        self.person.set_name('Jane Doe')
        self.assertEqual(self.person.get_name(), 'Jane Doe')

    def test_set_address(self):
        self.person.set_address('456 Avenue')
        self.assertEqual(self.person.get_address(), '456 Avenue')

    def test_get_address(self):
        self.assertEqual(self.person.get_address(), '123 Street')

    def test_is_homeless(self):
        self.assertEqual(self.person.is_homeless(), False)

if __name__ == '__main__':
    unittest.main()
