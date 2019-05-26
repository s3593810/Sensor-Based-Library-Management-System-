from unittest import mock
import unittest
import os
from validation import Validation


class TestValidation(unittest.TestCase):

    def test_passwordValidation_returnsTrue(self):
        valid = Validation()
        result = valid.passwordValidation("A12345")
        self.assertEqual(result, True)

    def test_passwordValidation_NoCapitalletter_returnsFalse(self):
        valid = Validation()
        result = valid.passwordValidation("a12345")
        self.assertEqual(result, False)

    def test_passwordValidation_LessThan6_returnsFalse(self):
        valid = Validation()
        result = valid.passwordValidation("a123")
        self.assertEqual(result, False)

    def test_passwordValidation_NumberOnly_returnsFalse(self):
        valid = Validation()
        result = valid.passwordValidation("476154")
        self.assertEqual(result, False)

    def test_passwordValidation_lettersOnly_returnsFalse(self):
        valid = Validation()
        result = valid.passwordValidation("Asdftr")
        self.assertEqual(result, False)

    def test_passwordMatching_returnsFalse(self):
        valid = Validation()
        result = valid.passwordMaching("A12345", "a12345")
        self.assertEqual(result, False)

    def test_passwordMatching_returnsTrue(self):
        valid = Validation()
        result = valid.passwordMaching("A12345", "A12345")
        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()
