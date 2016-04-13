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



# functional test
class CountMineInTableTest(unittest.TestCase):
    def test_num_mine_should_be_2(self):
        tabs_input = ["*...",\
                      "..*.", \
                      "...."]
        self.assertEqual( count_mine_in_table(tabs_input), 2)


# class CountMineAroundFieldTest(unittest.TestCase):
#
#     def test_mine_at_left_corner(self):
#         tabs_input = ["*...",\
#                       "..*.", \
#                       "...."]
#         tabs_output = ["*1..",\
#                       "11*.", \
#                       "...."]
#
#         self.assertEqual( count_mine_around_field(tabs_input, 0, 0), tabs_output)
