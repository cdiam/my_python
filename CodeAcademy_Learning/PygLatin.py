def pyglatin():
#Ask the user to enter a word
    answer = raw_input("Please type an English word here: ")

#Check the first two letters
    first_two_letters = answer[0:2]
    print first_two_letters

#Check if the answer is valid
    if len(answer) >0  and answer.isalpha():
        print answer
    else:
        print "Empty or non string"
        pyglatin()

pyglatin()
