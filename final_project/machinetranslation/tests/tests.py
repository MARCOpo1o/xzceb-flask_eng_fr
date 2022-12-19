'''tests for translation app'''
import unittest
from flask import url_for
from translator import english_to_french, french_to_english

class TestNullInput(unittest.TestCase):
    '''tests for null input'''
    def test_null_input(self):
        '''test null input'''
        self.assertEqual(english_to_french(''), '')
        self.assertEqual(french_to_english(''), '')

class TestTranslation(unittest.TestCase):
    '''tests for translation app'''
    def test_english_to_french(self):
        '''test english to french'''
        self.assertEqual(english_to_french('hello'), 'bonjour')

    def test_french_to_english(self):
        '''test french to english'''
        self.assertEqual(french_to_english('bonjour'), 'hello')

if __name__ == '__main__':
    unittest.main()

