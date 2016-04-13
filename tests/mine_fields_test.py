import unittest
from mine_fields import *


# Unit
class isMineTest(unittest.TestCase):

    def test_star_should_be_true(self):
        self.assertEqual( is_mine('*'), True)

    def test_dot_should_be_false(self):
        self.assertEqual( is_mine('.'), False)

class isFieldValidateTest(unittest.TestCase):

    def test_star_should_be_true(self):
        self.assertEqual( is_field_validate('*'), True)
    def test_dot_should_be_true(self):
        self.assertEqual( is_field_validate('.'), True)

    def test_a_should_be_false(self):
        self.assertEqual( is_field_validate('a'), False)
    def test_b_should_be_false(self):
        self.assertEqual( is_field_validate('b'), False)
    def test_C_should_be_false(self):
        self.assertEqual( is_field_validate('C'), False)
