#Harry Robinson
#22-10-2014
#Rogue value program

total = 0
counter = 0
finished = False


while not finished:
    number = float(input("Enter a number 'x'. Enter -1 when you have finished."))
    if number == -1:
        finished = True
    else:
        print("The program will carry on.")
        total = total + number
        counter = counter + 1
average = total / counter
print(average)
