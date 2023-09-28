def main():
    books = askBooks()
    calcPoints = calculatePoints(books)
    printAll(calcPoints)


def askBooks():
    books = int(input("How many books did you get this month?:"))
    return books

def calculatePoints(books):
    if(books == 0):
        points = 0
    if(books == 1):
        points = 5
    if(books == 2):
        points = 15
    if(books == 3):
        points = 30
    if(books >= 4):
        points = 60
    return points

def printAll(calcPoints):
    print("Number of points awarded:",calcPoints)

#Execute
main()