import unittest
import datetime


class TestDataAndTimeMethod(unittest.TestCase):
    def test_data_time_datatype(self):
        now=datetime.datetime.now()
        self.assertTrue(now,datetime)  # add assertion here


if __name__ == '__main__':
    unittest.main()
