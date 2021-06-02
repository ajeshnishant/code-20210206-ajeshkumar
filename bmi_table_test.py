import unittest
from bmi_table import *
from test_data import data


class TestBmi(unittest.TestCase):

    def test1(self):
        self.assertEqual(count_obese(data), 1)


if __name__ == "__main__":
    unittest.main()
