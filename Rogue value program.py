#Harry Robinson
#22-10-2014
#Rogue value program

total = 0
counter = 0

amountOfNumbers = int(input("Put the amount of numbers you want to enter: "))
while counter < amountOfNumbers:
    number = float(input("Please enter {0} in the series you wish to be averaged.Enter -1 when you have finished.".format(counter)))
    if number == -1:
        print("You have ended the program")
    else:
        print("The program will carry on.")
    total = total + number
    counter = counter + 1
average = total / amountOfNumbers
print(average)
