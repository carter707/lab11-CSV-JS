# https://github.com/carter707/lab11-CSV-JS.git
# Partner 1: Carter Veit
# Partner 2: Joshua Stanford


"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

def square_root(a): 
    if a < 0:
            raise ValueError

    return math.sqrt(a)# raise ValueError if a < 0

def hypotenuse(a, b): 
    return math.hypot(a, b) # can have negative nums

def add(a, b): 
    return a + b

def sub(a, b): 
    return a - b

def mul(a, b): 
    return a * b

def div(a, b): 
    if a == 0:
        raise ZeroDivisionError

    return b / a # raise ZeroDivisionError if a == 0

def log(a, b): 
    if a == 0:
        raise ValueError
    
    if b <= 0:
        raise ValueError

    return math.log(b,a) # use math library + raise ValueError

def exp(a, b):
    a ** b