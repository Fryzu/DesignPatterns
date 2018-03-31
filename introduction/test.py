import unittest
from code import Animal

class TestAnimal(unittest.TestCase):
    def testNameSetter(self):
        self.assertRaises(ValueError, lambda: Animal(name = '', weight = 100, sound = 'Woof'))
        self.assertRaises(ValueError, lambda: Animal(name = 151*'a', weight = 100, sound = 'Woof'))
        self.assertRaises(ValueError, lambda: Animal(name = ' sdfsdf', weight = 100, sound = 'Woof'))

if __name__ == '__main__':
    unittest.main()