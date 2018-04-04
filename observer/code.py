from abc import ABC, abstractmethod

# Subscribers

class Observer(ABC):
    @abstractmethod
    def update(self, updateData): #ducktyping
        pass

class DayMonthYear(Observer):
    def __init__(self, subject: Subject):
        subject.register(self)
        self.date = '-'

    def update(self, updateData):
        try:
            pass
        except:
            raise TypeError('updateData should be of Date type')    


# Notifiers

class Subject(ABC):
    def register(self, observer: Observer):