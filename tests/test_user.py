import unittest
from app.models import User
from app import db

class UserModelTest(unittest.TestCase):

    def setUp(self):
        self.new_user = User(password = 'kitsao')

    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)



    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('kitsao'))    