import unittest
from modules.merchant import Merchant

class TestMerchant(unittest.TestCase):

    def setUp(self):
        self.merchant = Merchant("Netflix", "An online streaming service and pandemic ditraction")

    def test_merchant_has_name(self):
        self.assertEqual("Netflix", self.merchant.name)

    def test_merchant_has_description(self):
        self.assertEqual("An online streaming service and pandemic ditraction", self.merchant.description)