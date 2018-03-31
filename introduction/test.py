import unittest
from code import Animal, Dog, Cat

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
    
if __name__ == '__main__':
    unittest.main()