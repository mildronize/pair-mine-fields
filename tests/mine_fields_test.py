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


class ReplaceCharInStringTest(unittest.TestCase):

    def test_center(self):
        self.assertEqual( replace_char_in_string('Hello', '$' ,3), 'Hel$o')
    def test_first(self):
        self.assertEqual( replace_char_in_string('Hello', '$', 0), '$ello')
    def test_last(self):
        self.assertEqual( replace_char_in_string('Hello', '$', 4), 'Hell$')

# functional test
class CountMineInTableTest(unittest.TestCase):
    def test_num_mine_should_be_2(self):
        tabs_input = ["*...",\
                      "..*.", \
                      "...."]
        self.assertEqual( count_mine_in_table(tabs_input), 2)

class MineFieldsTest(unittest.TestCase):
    def test_mine_field1(self):
        tabs_input = ["*...",\
                      "..*.", \
                      "...."]
        tabs_expect = ["*211",\
                       "12*1", \
                       "0111"]
        self.assertEqual( mine_fields(tabs_input), tabs_expect)

class ConvertDotToZeroTest(unittest.TestCase):
    def test_mine_1(self):
        tabs_input = ["*...",\
                      "..*.", \
                      "...."]
        tabs_expect = ["*000",\
                       "00*0", \
                       "0000"]
        self.assertEqual( convert_dot_to_zero(tabs_input), tabs_expect)

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
