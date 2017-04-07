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



def reverse(text):
    rev =""
    for i in text:
        rev = i + rev

    return rev
print reverse("cat")

def anti_vowel(text):
    result = text
    for char in text:
        if char in "aeiouAEIOU":
            result = result.replace(char, '')
    return result

print anti_vowel("Hey look Y Words!")


#scrabble_score

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}



def scrabble_score(word):
    word = word.lower()
    final_score = 0

    for i in word:
        final_score += score[i]

    return final_score

print scrabble_score("hello")

def censor(text,word):
    asterisks = "*" * len(word)
    censored = text.replace(word, asterisks)
    return censored

print censor("hello my name is Constantine, hello","hello")


def count(seq, item):
    total = 0
    for n in seq:
        if n == item:
            total = total +1
    return total


print count([1,5,4,3,2,5,5,5,5,5],5)

def purify(numbers):
    num = []
    for item in numbers:
        if item%2 == 0:
            num.append(item)
    return num

print purify([1,2,3,4,5,6])


 def product(lst):
    total = 1
    for i in lst:
        total *= i
    return total

print product([1,2,3,4])

def remove_duplicates(lst):
    numbers = []
    for n in lst:
        if n not in numbers:
            numbers.append(n)
    return numbers

print remove_duplicates([1,2,2,2,3,4,5])
