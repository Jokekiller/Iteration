#Harry Robinson
#23-10-2014
#Positive integer program

total = 1
count = 1

positiveInteger = int(input("Give a positive integer: "))
while positiveInteger < 0:
    print("Value must be greater than 0")
    positiveInteger = int(input("Give a positive integer: "))
while count <= positiveInteger:
    total = total * count
    count = count + 1
print("{0} factorial is {1}".format(positiveInteger,total))
