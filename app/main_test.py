from main import return_backward_string, get_mode
import unittest
import os

class TestMain(unittest.TestCase):

    def test_return_backward_string(self):
        random_string = "This is a test string"
        random_string_reversed = "gnirts tset a si sihT"
        self.assertEqual(return_backward_string(random_string), random_string_reversed)


    def test_get_mode(self):
        self.assertEqual(os.environ.get('MODE'), get_mode())

if __name__ == '__main__':
    unittest.main()