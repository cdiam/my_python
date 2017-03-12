####codeacademy Loops Lesson ####

count = 0

if count < 9:
    print "Hello, I am an if statement and count is", count

while count < 10:
    print "Hello, I am a while and count is", count
    count += 1



num = 1

while num < 11:  # Fill in the condition
    print num**2 # Print num squared
    num +=1 # Increment num (make sure to do this!)


choice = raw_input('Enjoying the course? (y/n)')

while choice !='y' and choice !='n':  # Fill in the condition (before the colon)
    choice = raw_input("Sorry, I didn't catch that. Enter again: ")


count = 0

while count < 10: # Add a colon
    print count
    count +=1# Increment count


import random

print "Lucky Numbers! 3 numbers will be generated."
print "If one of them is a '5', you lose!"

count = 0
while count < 3:
    num = random.randint(1, 6)
    print num
    if num == 5:
        print "Sorry, you lose!"
        break
    count += 1
else:
    print "You win!"




from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
# Start your game!


while guesses_left > 0 :
    guess = int(raw_input("Your guess: "))

    if guess == random_number:
        print "You win!"
        break

    guesses_left -=1

else:
    print "You lose. The number was %d" % random_number



thing = "spam!"

for c in thing:
    print c

word = "eggs!"

# Your code here!

for letter in word:
    print letter


phrase = "A bird in the hand..."

# Add your for loop

for char in phrase:
    if char =='A' or char == 'a':
        print 'X',

        '''
       The , character after our print statement means that our next print statement keeps printing on the same line.

        '''
    else:
        print char,




#Don't delete this print statement!
print


numbers  = [7, 9, 12, 54, 99]

print "This list contains: "

for num in numbers:
    print num

# Add your loop below!

for number in numbers:
    print number**2


##Dictionary print key and value

d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}

for key in d:
    # Your code here!

    print key, d[key]




choices = ['pizza', 'pasta', 'salad', 'nachos']

print 'Your choices are:'
for index, item in enumerate(choices):
    print index+1, item
