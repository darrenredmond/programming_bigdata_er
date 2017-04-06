import unittest

from Calculator import *

class TestCalculator(unittest.TestCase):
        
    def testadd(self):
        self.assertEqual(add(2,2),4)
        self.assertEqual(add(3,4),7)
        self.assertEqual(add(6,0),6)
        
    def testsubtract(self):
        self.assertEqual(subtract(2,2),0)
        self.assertEqual(subtract(4,2),2)
        self.assertEqual(subtract(10,6),4)
        
    def testmultiply(self):
        self.assertEqual(multiply(2,2),4)
        self.assertEqual(multiply(5,3),15)
        self.assertEqual(multiply(4,0),0)

    def testdivide(self):
        self.assertEqual(divide(4,1),4)
        self.assertEqual(divide(4,2),2)
        self.assertEqual(divide(2,2),1)
        self.assertEqual(divide(15,5),3)
        self.assertEqual(divide(5,0),'error')
  
        
    def testexponent(self):
        self.assertEqual(exponent(2,2),4)
        self.assertEqual(exponent(2,4),16)
        self.assertEqual(exponent(2,-2),0.25)
        self.assertEqual(exponent(2,0),1)
 

    def testsquare_root(self):
        self.assertEqual(square_root(4),2)
        self.assertEqual(square_root(16),4)
        self.assertEqual(square_root(36),6)

    def testsin(self):
        self.assertEqual(sin(0), 0)
        self.assertEqual(sin(10), 0.173648177)
        self.assertEqual(sin(20), 0.342020143)
        self.assertEqual(sin(50), 0.766044443)

    def testcos(self):
        self.assertEqual(cos(0), 1)
        self.assertEqual(cos(10), 0.984807753)
        self.assertEqual(cos(20), 0.93969262)
        self.assertEqual(cos(50), 0.642787609)

    def testtan(self):
        self.assertEqual(tan(0), 0)
        self.assertEqual(tan(10), 0.17632698)
        self.assertEqual(tan(20), 0.363970234)
        self.assertEqual(tan(50), 1.19175393)

    def testfactorial(self):
        self.assertEqual(factorial(8), 40320)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(5), 120)
    
if __name__ == '__main__':
    unittest.main()