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
