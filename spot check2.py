#Harry Robinson
#11-11-2014
#Iteration Spot check

number = 0
count = 0
answer = 0

number = int(input("Enter a number: "))
print("Times table for {0}".format(number))
for count in range(0,12):  
    count = count + 1
    answer = number * count
    print(" {0:>2} * {1:>2} = {2:>2}".format(count, number, answer))
    
    
