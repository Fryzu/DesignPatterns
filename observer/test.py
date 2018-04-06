import unittest
import datetime

from notifiers import *
from subscribers import *

class TestDayMonthYear(unittest.TestCase):

    def testFormat(self):
        testObj = DayMonthYear(None)

        _today = datetime.date.today()
        self.assertEqual(testObj.dateFormat(_today), \
        '{}.{}.{}'.format(_today.day, _today.month, _today.year))

if __name__ == '__main__':
    unittest.main()