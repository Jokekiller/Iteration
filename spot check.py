#Harry Robinson
#11-11-2014
#Iteration Spot check

number = 0
total = 0
while number != -1:
    number = int(input("Enter a number: "))
    total = total + (number*number)
if number == -1:
    total = total - 1
    print("the total is {0}".format(total))
