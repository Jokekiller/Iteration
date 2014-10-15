#Harry Robinson
#15-10-2014
#Program asking the amount of numbers to be averaged and then the numbers to be averaged

total = 0
counter = 0

amountOfNumbers = int(input("Give the amount of numbers you wish to be averaged: "))
while counter < amountOfNumbers:
    number = float(input("Please enter number {0} in the series you wish to be averaged".format(counter)))
    total = total + number
    counter = counter + 1
average = total / amountOfNumbers
print("The average of the numbers you entered is {0}.".format(average))
