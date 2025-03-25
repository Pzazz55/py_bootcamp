L85_UnitTest.py

import unittest
import L85_Capitalize as checkcap

class TestCap(unittest.TestCase):

    def test_one_word(self):
        text = 'python'
        result = checkcap.cap_text(text)
        self.assertEqual(result, 'Python')

    def test_multiple_word(self):
        text = 'monty python'
        result = checkcap.cap_text(text)
        self.assertEqual(result, 'Monty Python')

if __name__ == "__main__":
    unittest.main()