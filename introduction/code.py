const_maxNameLength = 150

class Animal:

    def __init__(self, name: str, weight: int, sound: str):
        self.name = name
        self.weight = weight
        self.sound = sound

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
        

