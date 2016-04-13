import unittest
from mine_fields import *


# Unit
class isMineTest(unittest.TestCase):

    def test_star_should_be_true(self):
        self.assertEqual( is_mine('*'), True)

    def test_dot_should_be_false(self):
        self.assertEqual( is_mine('.'), False)
