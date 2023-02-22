import unittest
from Triangle import classifyTriangle
class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testEquilateralTriangle1(self):
        self.assertEqual(classifyTriangle(2,2,2),'Equilateral')
    def testEquilateralTriangles2(self):
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral')

    def testRightTriangle3(self):
        self.assertEqual(classifyTriangle(3,4,5),'Right')

    def testRightTriangle4(self):
        self.assertEqual(classifyTriangle(5,3,4),'Right')
        
    def testScaleneTriangle5(self):
        self.assertEqual(classifyTriangle(3,6,7),'Scalene')

    def testScaleneTriangles6(self):
       self.assertEqual(classifyTriangle(11,14,23),'Scalene')

    def testNotATriangle7(self):
        self.assertEqual(classifyTriangle(1,1,20),'NotATriangle')

    def testNotATriangle8(self):
        self.assertEqual(classifyTriangle(5,5,25),'NotATriangle')

    def testInvalidInput9(self):
        self.assertEqual(classifyTriangle(-5,-9,-1),'InvalidInput')

    def testInvalidInput10(self):
        self.assertEqual(classifyTriangle(0,0,0),'InvalidInput')

    def testInvalidInput11(self):
        self.assertEqual(classifyTriangle(1.5,2.5,3.5),'InvalidInput')

    def testIsoscelesTriangle12(self):
        self.assertEqual(classifyTriangle(4, 4, 5), 'Isosceles')

    def testIsoscelesTriangle13(self):
        self.assertEqual(classifyTriangle(6, 9, 6), 'Isosceles')



if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()