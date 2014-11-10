#Harry Robinson
#10-11-2014
#Guess program

import random
count = 0
numberToGuess = random.randint(1,100)
while count != numberToGuess:
    number = int(input("Enter a number within range 1-100: "))
    count = count + 1
    if number > 100 or number < 1:
        count = count - 1
        print("Enter a number within the range")
    elif number < numberToGuess:
        print("number to low")
    elif number > numberToGuess:
        print("number to high")
    else:
        print("Number correct: this took you {0} attempts".format(count))

