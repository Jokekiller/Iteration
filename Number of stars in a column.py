#Harry Robinson
#25-10-2014
#Number of stars per row and column

starsPerRow = 0
numberOfRows = 0
rowNumber = 0
starCount = 0
starString = ""

starsPerRow = int(input("Enter the number of stars per row: "))
numberOfRows = int(input("Enter the number of rows you want to be printed: "))
for rowNumber in range(numberOfRows):
    for starCount in range(starsPerRow):
        starString = starString + "*"
    print(starString)
    starString = ""

