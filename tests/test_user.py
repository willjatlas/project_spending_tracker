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

    def test_user_has_email(self):
        self.assertEqual("troybarnes@taaitm.com", self.user.email)
    
    def test_user_has_wallet(self):
        self.assertEqual(250.00, self.user2.wallet)
    
    def test_user_is_charged(self):
        self.user.charge_wallet(19.50)
        self.assertEqual(140.50, self.user.wallet)

    def test_user_can_add_funds(self):
        self.user2.add_to_wallet(14.20)
        self.assertEqual(264.20, self.user2.wallet)

    def test_user_can_afford(self):
        self.assertTrue(self.user2.can_affort(100))