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
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(1,0)


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
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################
#on edstream after I push, then tell to pull
# Do not touch this
if __name__ == "__main__":
    unittest.main()