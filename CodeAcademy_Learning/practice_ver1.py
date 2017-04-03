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



def digit_sum(x):
  string_x = str(x)
  total = 0
  for char in string_x:
    total += int(char)
  return total


def factorial(x):
    product = 1
    for i in range(x):
        product = product * (i + 1)
    return product

print factorial(4)



x = int(raw_input ("Give me a number"))

def is_prime(x):
    if x < 2:
        return False
    elif x >3:
        for n in range (2, x-1):
            if (x % n) == 0:
                return False
                n += 1
        else:
            return True
    elif x == 2 or x == 3 :
        return True
