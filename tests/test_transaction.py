import unittest
from modules.transaction import Transaction
from modules.user import User
from modules.tag import Tag
from modules.merchant import Merchant

class testTransaction(unittest.TestCase):

    def setUp(self):
        self.user = User("Ben", "Chang", "changsyaboi@taaitm.com", 145.60)
        self.merchant = Merchant("Scotmid", "General grocieries and provider of snax")
        self.tag = Tag("Snacks")
        self.transaction = Transaction("11/05/20", "19:40", 6.50)

    def test_transaction_has_date(self):
        self.assertEqual("11/05/20", self.transaction.date)

    def test_transaction_has_time(self):
        self.assertEqual("19:40", self.transaction.time)

    def test_transaction_has_amount(self):
        self.assertEqual(6.50, self.transaction.amount)

    def test_transaction_has_user(self):
        self.assertEqual(self.user, self.transaction.user)

    def test_transaction_has_merchant(self):
        self.assertEqual(self.merchant, self.transaction.merchant)
    
    def test_transaction_has_tag(self):
        self.assertEqual(6.50, self.transaction.tag)
        
