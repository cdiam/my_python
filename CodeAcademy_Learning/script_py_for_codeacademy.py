#!/usr/bin/python

#This is the scripts from codeacademy
#Set spam equal to 1 using modulo on line 3!


spam =3%2

span2 = 4%2

print "The first is %d and the second is %d" % (spam, span2)


# Tip Calculator!

meal = 44.50
tax = 0.0675
tip = 0.15

meal = meal + meal * tax
total = meal + (meal * tip)

print("%.2f" % total)


#print letter

fifth_letter = "MONTY"[4]

print fifth_letter


ministry = "The Ministry of Silly Walks"

print len(ministry)
print ministry.upper()


# Print the concatenation of "Spam and eggs" on line below!

print"Spam "+"and "+"eggs"

# Turn 3.14 into a string on line below!

print "The value of pi is around " + str(3.14)

string_1 = "Camelot"
string_2 = "place"

print "Let's not go to %s. 'Tis a silly %s." % (string_1, string_2)


name = raw_input("What is your name?")
quest = raw_input("What is your quest?")
color = raw_input("What is your favorite color?")

print "Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color)



# Write your code below, starting on line below!

my_string = "Constantine"
print len(my_string)
print my_string.upper()



###########DATE AND TIME ################

from datetime import datetime
now = datetime.now()

print now
print now.year
print now.month
print now.day

print '%s/%s/%s' % (now.month, now.day, now.year)
print '%s:%s:%s' % (now.hour, now.minute, now.second)

print '%s/%s/%s %s:%s:%s' % (now.month,now.day,now.year,now.hour, now.minute, now.second)



#############SECTION Conditionals & Control Flow ##################

def clinic():
    print "You've just entered the clinic!"
    print "Do you take the door on the left or the right?"
    answer = raw_input("Type left or right and hit 'Enter'.").lower()
    if answer == "left" or answer == "l":
        print "This is the Verbal Abuse Room, you heap of parrot droppings!"
    elif answer == "right" or answer == "r":
        print "Of course this is the Argument Room, I've told you that already!"
    else:
        print "You didn't pick left or right! Try again."
        clinic()

clinic()



# Assign True or False as appropriate on the lines below!

# Set this to True if 17 < 328 or to False if it is not.
bool_one = True   # We did this one for you!

# Set this to True if 100 == (2 * 50) or to False otherwise.
bool_two = True

# Set this to True if 19 <= 19 or to False if it is not.
bool_three = True

# Set this to True if -22 >= -18 or to False if it is not.
bool_four = False

# Set this to True if 99 != (98 + 1) or to False otherwise.
bool_five = False


"""
     Boolean Operators
------------------------      True and True is True
True and False is False
False and True is False
False and False is False

True or True is True
True or False is True
False or True is True
False or False is False

Not True is False
Not False is True

"""

# Use boolean expressions as appropriate on the lines below!

# Make me false!
bool_one = (2 <= 2) and "Alpha" == "Bravo"  # We did this one for you!

# Make me true!
bool_two = (1+1) == 2 and (2+2)==4

# Make me false!
bool_three = (5-0)<1 or "my"=="your"

# Make me true!
bool_four = True and not not True

# Make me true!
bool_five = (2+2)==4 or (5+5)==10

### Conditional Statement Syntax ####

response = "Y"

answer = "Left"
if answer == "Left":
    print "This is the Verbal Abuse Room, you heap of parrot droppings!"

# Will the above print statement print to the console?
# Set response to 'Y' if you think so, and 'N' if you think not.


def using_control_once():
    if 2==2:
        return "Success #1"

def using_control_again():
    if "A"=="A":
        return "Success #2"

print using_control_once()
print using_control_again()


###The else statement complements ####

answer = "'Tis but a scratch!"

def black_knight():
    if answer == "'Tis but a scratch!":
        return True
    else:
        return False       # Make sure this returns False

def french_soldier():
    if answer == "Go away, or I shall taunt you a second time!":
        return True
    else:
        return False       # Make sure this returns False


#elif#

def greater_less_equal_5(answer):
    if answer>5:
        return 1
    elif answer<5:
        return -1
    else:
        return 0

print greater_less_equal_5(4)
print greater_less_equal_5(5)
print greater_less_equal_5(6)


# Make sure that the_flying_circus() returns True
def the_flying_circus():
    if (3==3) and (4==4):    # Start coding here!
        return True

    elif 3<1:
        return "No this is false"

    else:
        return "This is equal"

the_flying_circus()



###FUNCTION SECTIONS ####

def tax(bill):
    """Adds 8% tax to a restaurant bill."""
    bill *= 1.08
    print "With tax: %f" % bill
    return bill

def tip(bill):
    """Adds 15% tip to a restaurant bill."""
    bill *= 1.15
    print "With tip: %f" % bill
    return bill

meal_cost = 100
meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_with_tax)


def square(n):
    """Returns the square of a number."""
    squared = n**2
    print "%d squared is %d." % (n, squared)
    return squared

# Call the square function on line 9! Make sure to
# include the number 10 between the parentheses.
square(10)


def power(base, exponent):  # Add your parameters here!
    result = base**exponent
    print "%d to the power of %d is %d." % (base, exponent, result)

power(37,4)  # Add your arguments here!


def one_good_turn(n):
    return n + 1

def deserves_another(n):
    return one_good_turn(n) + 2


def cube(number):
    return number**3

def by_three(number):
    if number % 3 ==0:
      result =cube(number)
      return result
    else:
        return False

print cube(9)
print by_three(9)


def biggest_number(*args):
    print max(args)
    return max(args)

def smallest_number(*args):
    print min(args)
    return min(args)

def distance_from_zero(arg):
    print abs(arg)
    return abs(arg)


biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)


def distance_from_zero(argument):
    if type(argument) == int or type(argument) == float:
        return abs(argument)
    else:
        return "Nope"





#### Python Lists and Dictionaries ###
zoo_animals = ["pangolin", "cassowary", "sloth", "tiger"];
# One animal is missing!

if len(zoo_animals) > 3:
	print "The first animal at the zoo is the " + zoo_animals[0]
	print "The second animal at the zoo is the " + zoo_animals[1]
	print "The third animal at the zoo is the " + zoo_animals[2]
	print "The fourth animal at the zoo is the " + zoo_animals[3]



numbers = [5, 6, 7, 8]

print "Adding the numbers at indices 0 and 2..."
print numbers[0] + numbers[2]
print "Adding the numbers at indices 1 and 3..."
print numbers[1] + numbers[3]


zoo_animals = ["pangolin", "cassowary", "sloth", "tiger"]
# Last night our zoo's sloth brutally attacked
#the poor tiger and ate it whole.

# The ferocious sloth has been replaced by a friendly hyena.
zoo_animals[2] = "hyena"

# What shall fill the void left by our dear departed tiger?
zoo_animals[3] = "cat"


suitcase = []
suitcase.append("sunglasses")

# Your code here!
suitcase.append("phone")
suitcase.append("charger")
suitcase.append("shoes")



list_length = len(suitcase)# Set this to the length of suitcase

print "There are %d items in the suitcase." % (list_length)
print suitcase

animals = "catdogfrog"
cat  = animals[:3]   # The first three characters of animals
dog  = animals[3:6]              # The fourth through sixth characters
frog = animals[6:]              # From the seventh character to the end



animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")    # Use index() to find "duck"
print duck_index
# Your code here!

animals.insert(duck_index, "cobra")

print animals # Observe what prints after the insert operation


my_list = [1,9,3,8,5,7]

for number in my_list:
    print 2 * number # Your code here


start_list = [5, 3, 1, 2, 4]
square_list = []

# Your code here!

for x in start_list:
    square_list.append(x ** 2)

square_list.sort()
print square_list



####python list and dictionaries ###

# Assigning a dictionary with three key-value pairs to residents:
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}

print residents['Puffin'] # Prints Puffin's room number

# Your code here!
print residents['Sloth']
print residents['Burmese Python']


menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print menu['Chicken Alfredo']

# Your code here: Add some dish-price pairs to menu!
menu['Spam'] = 12
menu['Burger'] = 29.12
menu['potato'] = 35.12



print "There are " + str(len(menu)) + " items on the menu."
print menu




# key - animal_name : value - location
zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}
# A dictionary (or list) declaration may break across multiple lines

# Removing the 'Unicorn' entry. (Unicorns are incredibly expensive.)
del zoo_animals['Unicorn']
del zoo_animals['Sloth']
del zoo_animals['Bengal Tiger']

# Your code here!
zoo_animals['Rockhopper Penguin'] = 'Entry House'



print zoo_animals



###removing item from list ####

backpack = ['xylophone', 'dagger', 'tent', 'bread loaf']
backpack.remove("dagger")




inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort()

# Your code here
inventory['pocket'] = ['seashell', 'strange berry', 'lint']

inventory['backpack'].sort()
print inventory['backpack']
inventory['backpack'].remove("dagger")
inventory['gold'] = inventory['gold'] + 50


names = ["Costas","Adam","Alex","Mariah","Martine","Columbus"]

names.sort()

for name in names:
    print name


webster = {
	"Aardvark" : "A star of a popular children's cartoon show.",
    "Baa" : "The sound a goat makes.",
    "Carpet": "Goes on the floor.",
    "Dab": "A small amount."
}

# Add your code below!

for key in webster:
    print webster[key]


a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


for x in a:
    if x % 2 == 0:
        print x


for letter in "Codecademy":
    print letter

# Empty lines to make the output pretty
print
print

word = "Programming is fun!"

for letter in word:
    # Only print out the letter i
    if letter == "i":
        print letter




prices = {
"banana": 4,
"apple": 2,
"orange": 1.5,
"pear": 3
}

stock = {
"banana": 6,
"apple": 0,
"orange": 32,
"pear": 15,
}

for key in prices:
    print "%s" % key
    print "price: %s" % prices[key]
    print "stock: %s" % stock[key]



prices = {
    "banana" : 4,
    "apple"  : 2,
    "orange" : 1.5,
    "pear"   : 3,
}
stock = {
    "banana" : 6,
    "apple"  : 0,
    "orange" : 32,
    "pear"   : 15,
}
total = 0

for key in prices:
    print key
    money = prices[key] * stock[key]
    print "Money= %s" % money
    total = total + money

print total


n = [1, 3, 5]
# Do your multiplication here
k = n[1]*5
n[1]=k
print n


n = [1, 3, 5]
# Remove the first item in the list here
n.pop(0)
print n


m = 5
n = 13
# Add add_function here!

def add_function(x,y):

    adding_number = x + y

    return adding_number

print add_function(m, n)


n = "Hello"
# Your function here!

def string_function(s):
    return s + "world"


print string_function(n)



def list_function(x):
    return x[1]

n = [3, 5, 7]
print list_function(n)


#
#Change list_function so that:
#Add 3 to the item at index one of the list.
#Store the result back into index one.
#eturn the list.

def list_function(x):
    x[1] = x[1]+3
    return x

n = [3, 5, 7]
print list_function(n)


n = [3, 5, 7]
# Add your function here
def list_extender(lst):
    lst.append(9)
    return lst


print list_extender(n)


n = [3, 5, 7]

def print_list(x):
    for i in range(0, len(x)):
        print x[i]

print print_list(n)

n = [3, 5, 7]

def double_list(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x
# Don't forget to return your new list!

print double_list(n)
