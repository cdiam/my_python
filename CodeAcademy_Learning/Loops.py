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
