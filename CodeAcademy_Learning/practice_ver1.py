#Practice Makes Perfect
'''
All right! Let's get started.

Remember how an even number is a number that is divisible by 2?

'''

def is_even(x):
    if x % 2 == 0 :
        return True
    else:
        return False


import math

def is_int(x):
    if x == round(x):
        return True
    else:
        return False
