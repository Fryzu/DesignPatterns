#from __future__ import annotations

from abc import ABC, abstractmethod

class Subject(ABC):
    def __init__(self):
        self._observersList = []

    def register(self, observer: 'Observer'):
        self._observersList.append(observer)

    def unregister(self, observer: 'Observer'):
        try:
            self._observersList.remove(observer)
        except ValueError:
            raise ValueError('No such a observer in the observers list')

    def __str__(self):
        return "Amount of observers: {}".format(len(self._observersList))

    @abstractmethod
    def notify(self):
        pass

class ActualTime(Subject):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def notify(self):
        dateToSend = datetime.date.today()

        for i in self._observersList:
            i.update(dateToSend)

    
        
