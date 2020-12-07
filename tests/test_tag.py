import unittest
from models.tag import Tag

class TestTag(unittest.TestCase):

    def setUp(self):
        self.tag = Tag("Buisness")
    
    def test_tag_has_type(self):
        self.assertEqual("Buisness", self.tag.tag_type)
