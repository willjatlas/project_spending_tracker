import unittest
from modules.user import User 

class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = User("Troy", "Barnes", "troybarnes@taaitm.com", 160.00)
        self.user2 = User("Abed", "Nadir", "abednadir@taaitm.com", 250.00)

    def test_user_has_first_name(self):
        self.assertEqual("Troy", self.user.first_name)

    def test_user_has_last_name(self):
        self.assertEqual("Nadir", self.user2.last_name)