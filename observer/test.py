import unittest
import datetime

from notifiers import *
from subscribers import *

class TestDayMonthYear(unittest.TestCase):

    def testFormat(self):
        testSubject = ActualTime()
        testObj = DayMonthYear(testSubject)

        _today = datetime.date.today()
        self.assertEqual(testObj.dateFormat(_today), \
        '{}.{}.{}'.format(_today.day, _today.month, _today.year))

    def testDateGetter(self):
        testSubject = ActualTime()
        testObj = DayMonthYear(testSubject)

        self.assertEqual(testObj.date, '-')

class TestSubject(unittest.TestCase):
    
    def testRegister(self):
        testSubject = ActualTime()

        testObj1 = DayMonthYear(testSubject)
        testObj2 = DayMonthYear(testSubject)
        testObj3 = DayMonthYear(testSubject)

        self.assertEqual(str(testSubject), 'Amount of observers: 3')

class TestDayMonthYear(unittest.TestCase):
    def testNotify(self):
        pass

if __name__ == '__main__':
    unittest.main()