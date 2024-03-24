import unittest
import os
import sys
from mod5.Redirect import Redirect

class TestRedirect(unittest.TestCase):
    def test_stdout(self):
        stdout_file = open('stdout.txt', 'w')
        with Redirect(stdout=stdout_file):
            print('Hello stdout.txt')
        stdout_file.close()
        with open('stdout.txt', 'r') as f:
            self.assertEqual(f.read(), 'Hello stdout.txt\n')
        os.remove('stdout.txt')

    def test_stderr(self):
        stderr_file = open('stderr.txt', 'w')
        with self.assertRaises(Exception):
            with Redirect(stderr=stderr_file):
                raise Exception('Hello stderr.txt')
        stderr_file.close()
        with open('stderr.txt', 'r') as f:
            self.assertTrue('Hello stderr.txt' in f.read())
        os.remove('stderr.txt')

    def test_stdout_and_stderr(self):
        stdout_file = open('stdout.txt', 'w')
        stderr_file = open('stderr.txt', 'w')
        with self.assertRaises(Exception):
            with Redirect(stdout=stdout_file, stderr=stderr_file):
                print('Hello stdout.txt')
                raise Exception('Hello stderr.txt')
        stdout_file.close()
        stderr_file.close()
        with open('stdout.txt', 'r') as f:
            self.assertEqual(f.read(), 'Hello stdout.txt\n')
        with open('stderr.txt', 'r') as f:
            self.assertTrue('Hello stderr.txt' in f.read())
        os.remove('stdout.txt')
        os.remove('stderr.txt')

if __name__ == '__main__':
    unittest.main()
