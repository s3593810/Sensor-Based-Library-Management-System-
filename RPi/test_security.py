from unittest import mock
import unittest
import os
from security import Security


class TestSecurity(unittest.TestCase):

    def test_encryptAndDecrypt_returnsSamePassword(self):
        security = Security()
        result = security.encrypt("A12345", "a")
        decryptResult = security.decrypt(result, "a")
        self.assertEqual(
            decryptResult, b'A12345')

    def test_encryptAndDecrypt_returnsincorrectpasword(self):
        security = Security()
        result = security.encrypt("A12345", "a")
        decryptResult = security.decrypt(result, "a")
        self.assertNotEqual(
            decryptResult, b'S12345')


if __name__ == '__main__':
    unittest.main()
