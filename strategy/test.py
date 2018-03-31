import unittest
from code import *

class TestAnimal(unittest.TestCase):
    def testNameSetter(self):
        self.assertRaises(ValueError, lambda: Animal(name = '', weight = 100))
        self.assertRaises(ValueError, lambda: Animal(name = 151*'a', weight = 100))
        self.assertRaises(ValueError, lambda: Animal(name = ' sdfsdf', weight = 100))

class TestDog(unittest.TestCase):
    def testInit(self):
        testDog = Dog(name = 'Buffy', weight = 30)

        self.assertEqual(testDog.sound, 'Woof woof!')
        self.assertEqual(testDog.digHole(), 'Woof woof! <<digging a hole>> Woof woof!')
    
class TestCat(unittest.TestCase):
    def testInit(self):
        testCat = Cat(name = 'Mrau', weight = 10)

        self.assertEqual(testCat.sound, 'Miauu miauuu')
    
class TestFlying(unittest.TestCase):
    def testFly(self):
        testBird = Bird(name = 'Dziobak', weight = 2)
        testDog = Dog(name = 'Buffy', weight = 30)
        
        self.assertEqual(testBird.flying.fly(), 'I am flying really high')
        self.assertEqual(testDog.flying.fly(), 'I cannot fly!!')

if __name__ == '__main__':
    unittest.main()