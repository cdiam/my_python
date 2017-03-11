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
