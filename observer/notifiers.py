#from __future__ import annotations

from abc import ABC, abstractmethod

class Subject(ABC):
    def register(self, observer: 'Observer'):
        pass

class ActualTime(Subject):
    pass