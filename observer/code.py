from abc import ABC, abstractmethod
import datetime

# Subscribers

class Observer(ABC):
    @abstractmethod
    def update(self, updateData): #ducktyping
        pass

class DayMonthYear(Observer):
    def __init__(self, subject: Subject):
        '''subject.register(self)
        self.date = '-' '''
        pass

    def update(self, updateData):
        '''try:
            pass
        except:
            raise TypeError('updateData should be of Date type')   '''

        pass

    def format(date: datetime.date):
        return '{}.{}.{}'.format(date.day, date.month, date.day)

# Notifiers

class Subject(ABC):
    def register(self, observer: Observer):
        pass

class ActualTime(Subject):
    pass