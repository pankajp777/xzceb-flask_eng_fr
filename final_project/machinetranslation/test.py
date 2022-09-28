import unittest
from  translator import *

class TestEnglishToFrench(unittest.TestCase):

    def test_en_fr1(self):
        self.assertEqual(english_to_french("Hello"), 'Bonjour')

    def test_en_fr2(self):
         self.assertNotEqual(english_to_french(""), " the 'text' empty.")


class TestFrenchToEnglish(unittest.TestCase):

        
    def test_fr_en1(self):
        self.assertEqual(french_to_english("Bonjour"), 'Hello')

    def test_fr_en2(self):
        self.assertNotEqual(french_to_english(""), " the 'text' empty.")


if __name__ == '__main__':
    unittest.main()