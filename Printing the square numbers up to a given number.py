#Harry Robinson
#04-11-2014
#Printing the number squares up to an entered number

count = 1
squareNumber = 1

number = int(input("Enter a number: "))
for count in range(number):
    squareNumber = count **2
    print("{0:>2} squared is {1:^ 2}".format(count, squareNumber))
    count = count + 1
    
