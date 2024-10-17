
import unittest
import datetime

class TestDataAndTimeMethod(unittest.TestCase):

    def test_data_time_datatype(self):
        now=datetime.datetime.now()
        t=now.strftime("%H:%M:%S")
        s1=now.strftime("%m%d%Y, %H:%M:%S")
        self.assertTrue(now,datetime)


    def test_date_datatype(self):
        current_date=datetime.date.today()
        self.assertTrue(current_date, datetime.date)

    def test_datatype_var(self):
        d=datetime.date(2022,12,25)
        self.assertTrue(d, datetime.date)

    def test_todayDate(self):
        todays_date= datetime.date.today()
        self.assertTrue(todays_date,datetime.date)

    def test_timestamp(self):
        timestamp= datetime.date.fromtimestamp(1326244364)
        self.assertTrue(timestamp,datetime.date)

    def test_today(self):
        today= datetime.date.today()
        self.assertTrue(today,datetime.date)



if __name__ == '__main__':
    unittest.main()
