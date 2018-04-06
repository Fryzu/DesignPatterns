from abc import ABC, abstractmethod
import datetime

class Observer(ABC):
    @abstractmethod
    def update(self, updateData: datetime.date):
        pass

class DayMonthYear(Observer):
    def __init__(self, subject: 'Subject'):
        subject.register(self)
        actualDate = '-'

    def update(self, updateData: datetime.date):
        self.actualDate = dateFormat(updateData)

    def dateFormat(self, _date: datetime.date):
        return '{}.{}.{}'.format(_date.day, _date.month, _date.year)
