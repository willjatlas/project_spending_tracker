import unittest
from modules.transaction import Transaction

class testTransaction(unittest.TestCase):

    def setUp(self):
        self.transaction = Transaction("11/05/20", "19:40", 6.50)

    def test_transaction_has_date(self):
        self.assertEqual("11/05/20", self.transaction.date)

    def test_transaction_has_time(self):
        self.assertEqual("19:40", self.transaction.time)

    def test_transaction_has_amount(self):
        self.assertEqual(6.50, self.transaction.amount)
