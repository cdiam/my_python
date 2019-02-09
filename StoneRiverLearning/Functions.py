
# Functions

def addition(num1,num2):
    answer = num1 + num2 
    return answer

x = addition(5,6)
print(x)


def website( font="arial", font_color="black", background = 'grey'):
    print('font:', font)
    print('font_color', font_color)


website(background='black')



x = 10

def example():
    z = 5
    print(z)

def example2():
    z = 7
    print(z)
    print(x)
    y = x +1 
    print(y)

example()

example2()

def example3():
    z=10
    print("The latest z for example3 is:",z)

example3()

my_dict = {
  "name": "Constantine",
  "age": 42,
  "family": True
  
}

print my_dict.keys()
print my_dict.values()


my_dict = {
  'name': 'Nick',
  'age':  31,
  'occupation': 'Dentist',
}

for key in my_dict:
  print key, my_dict[key]


  evens_to_50 = [i for i in range(51) if i % 2 == 0]
print evens_to_50

new_list = [x for x in range(1, 6)]
# => [1, 2, 3, 4, 5]

doubles = [x * 2 for x in range(1, 6)]
# => [2, 4, 6, 8, 10]

doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]
# => [6]


# Complete the following line. Use the line above for help.
even_squares = [x * x for x in range(1,11) if x % 2 == 0 ]

print even_squares


cubes_by_four = [x * x * x  for x in range (11) if x>= 1 and x <= 10 if (x * x * x) % 4 == 0]

print cubes_by_four


l = [i ** 2 for i in range(1, 11)]
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print l[2:9:2]


my_list = range(1, 11) # List of numbers 1 - 10

# Print odd numbers.Add your code below!
print my_list[::2]


my_list = range(1, 11)

# Create a variable called backwards and set it equal to the reversed version of my_list.Add your code below!
backwards = my_list[::-1]