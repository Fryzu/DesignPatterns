from abc import ABC, abstractmethod

# Strategy pattern

class FlyStrategy(ABC):
    @abstractmethod
    def fly() -> str:
        pass

class CanFly(FlyStrategy):
    def fly() -> str:
        return 'I am flying really high'

class CantFly(FlyStrategy):
    def fly() -> str:
        return 'I cannot fly!!'

# Animals

const_maxNameLength = 150

class Animal:

    def __init__(self, name: str, weight: int, sound: str = None, flying: FlyStrategy = CantFly):
        self.name = name
        self.weight = weight
        self.sound = sound
        self.flying = flying

    @property 
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        if name == '':
            raise ValueError('Animal name cannot be empty')
        if name[0] == ' ':
            raise ValueError('Animal name cannot start with blank character')
        if len(name) > const_maxNameLength:
            raise ValueError('Animal name too long')
        self._name = name
        

class Dog(Animal):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.sound = 'Woof woof!'
        self.flying = CantFly

    def digHole(self):
        return ('{0} <<digging a hole>> {0}'.format(self.sound))

class Cat(Animal):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.sound = 'Miauu miauuu'
        self.flying = CantFly

class Bird(Animal):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.sound = 'Gruuu duuu gruu'
        self.flying = CanFly