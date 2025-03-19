import unittest
from unittest.mock import patch
from io import StringIO
from src.main import main

class TestMain(unittest.TestCase):
    """Test cases for the main function in main.py"""

    def test_main_exists(self):
        """Test if the main function exists and is callable"""
        self.assertTrue(callable(main))

    @patch('sys.stdout', new_callable=StringIO)
    def test_main_output(self, mock_stdout):
        """Test if the main function prints the correct message"""
        main()
        self.assertEqual(mock_stdout.getvalue().strip(), "Hello, this is the first time!")

if __name__ == '__main__':
    unittest.main()