# https://github.com/carter707/lab11-CSV-JS.git
# Partner 1: Carter Veit
# Partner 2: Joshua Stanford

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    def test_add(self):
        self.assertEqual(add(3,-3),0)
        self.assertEqual(add(5,9),14)
        self.assertEqual(add(2, -7), -5)

    # def test_subtract(self): # 3 assertions
    def test_subtract(self):
        self.assertEqual(sub(5, 4),1)
        self.assertEqual(sub(-7, -2), -5)
        self.assertEqual(sub(0, 2), -2)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(0, mul(1000, 0))
        self.assertEqual(9, mul(4.5, 2))
        self.assertEqual(-23304, mul(23304, -1))

    def test_divide(self): # 3 assertions
        self.assertEqual(5, div(2, 10))
        self.assertAlmostEqual(-3.333333, div(-3, 10), 3)
        self.assertEqual(30, div(0.3, 9))

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0,1)


    # def test_logarithm(self): # 3 assertions
    def test_logarithm(self):
        self.assertEqual(log(100,10), 2)
        self.assertEqual(log(16 ,2), 4)
        self.assertEqual(log(25, 5), 2)
    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            log(8, 0)
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        # call log function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     logarithm(0, 5)

        with self.assertRaises(ValueError):
            log(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(5, hypotenuse(3,4))
        self.assertAlmostEqual(1.414213, hypotenuse(1,1), 4)
        self.assertEqual(10, hypotenuse(-6,8))

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #    square_root(NUM)
        # Test basic function
        with self.assertRaises(ValueError):
            square_root(-1)
        self.assertEqual(4, square_root(16))
        self.assertAlmostEqual(1.414213, square_root(2), 4)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()