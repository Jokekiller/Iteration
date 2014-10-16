#Harry Robinson
#16-10-2014
#Expressing a range


inputString = "Give your number (10-20): "
number = int(input(inputString))
while number < 10 or number > 20:
    print("Enter a number in the range")
    number = int(input(inputString))
print("Number {0} is in the range".format(number))
