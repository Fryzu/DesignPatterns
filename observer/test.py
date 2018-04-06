import unittest
from code import *
import datetime

class TestDayMonthYear(unittest.TestCase):
    
    def testObjects(self):
        testSubject = ActualTime()
        testObj = DayMonthYear(testSubject)
    
    def testFormat(self):
        today = date.today()

        self.assertEqual(testObj.format(today), \
        '{}.{}.{}'.format(today.day, today.month, today.day))