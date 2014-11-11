#Harry Robinson
#11-11-2014
#Spot check

import random
random.randint(1,100)

guessed = False
number = random.randint(1,100)
noOfTurns = 0

while guessed == False:
    userGuess = int(input("Enter your guess for the number: "))
    noOfTurns = noOfTurns + 1
    if userGuess > number:
        print("Number is too high")
    else:
        print("Number is too low")
    if userGuess == number:
        print("You took {0} guess' to get the number".format(noOfTurns))
        print("The number was {0}".format(number))


        
        
