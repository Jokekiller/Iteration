#Harry Robinson
#28-10-2014
#Program stating the largest of a vlue of entered numbers

maximum = 0
numberInSeries = 0
finished = False

while not finished:
    numberInSeries = float(input("Enter a number in the series and the -1 to finish it: "))
    if numberInSeries == -1:
        finished = True
    elif numberInSeries > maximum:
        maximum = numberInSeries
print("Max value is: {0}".format(maximum))
        
