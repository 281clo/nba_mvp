import unittest

class TestFunc(unittest.TestCase):
    
    def test_func1(self):
        self.assertEqual(funcfile.func1(3,4), 0.75)
        self.assertEqual(funcfile.func1(-4,2), -2)
        self.assertRaises(ValueError, funcfile.func1, 7, 0)
    
    def test_func2(self):
        self.assertEqual(funcfile.func2(3), '1 22 333')
        #two more

if __name__ == '__main__':
    unittest.main()