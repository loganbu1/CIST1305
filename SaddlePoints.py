NUM_ROWS = 7
NUM_COLUMNS = 7

import random

def main():
    saddlePoints()

def saddlePoints():
    totalSaddlePoints = 0

    saddleArray = [ [0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0], ]
    row = 0
    while(row < NUM_ROWS):
        col = 0
        while(col < NUM_COLUMNS):
            saddleArray[row][col] = random.randint(1,10)
            print(saddleArray[row][col])
            col += 1
        row += 1

    row = 0
    while(row < NUM_ROWS):
        col = 0
        while(col < NUM_COLUMNS):
            currentElement = saddleArray[row][col]
            if(row == 0):
                currentElement <= saddleArray[row][col+1] and currentElement <= saddleArray[row][col+2] and currentElement <= saddleArray[row][col+3] and currentElement <= saddleArray[row][col+4] and currentElement <= saddleArray[row][col+5] and currentElement <= saddleArray[row][col+5]
                print("Saddlepoint found",currentElement)
            if(row == 1):
                currentElement <= saddleArray[row][col-1] and currentElement <= saddleArray[row][col+1] and currentElement <= saddleArray[row][col+2] and currentElement <= saddleArray[row][col+3] and currentElement <= saddleArray[row][col+4] and currentElement <= saddleArray[row][col+4]
                print("Saddlepoint found",currentElement)
            if(row == 2):
                currentElement <= saddleArray[row][col-2] and currentElement <= saddleArray[row][col-1] and currentElement <= saddleArray[row][col+1] and currentElement <= saddleArray[row][col+2] and currentElement <= saddleArray[row][col+3] and currentElement <= saddleArray[row][col+3]
                print("Saddlepoint found",currentElement)
            if(row == 3):
                currentElement <= saddleArray[row][col-3] and currentElement <= saddleArray[row][col-2] and currentElement <= saddleArray[row][col-1] and currentElement <= saddleArray[row][col+1] and currentElement <= saddleArray[row][col+2] and currentElement <= saddleArray[row][col+2]
                print("Saddlepoint found",currentElement)
            if(row == 4):
                currentElement <= saddleArray[row][col-4] and currentElement <= saddleArray[row][col-3] and currentElement <= saddleArray[row][col-2] and currentElement <= saddleArray[row][col-1] and currentElement <= saddleArray[row][col+1] and currentElement <= saddleArray[row][col+1]
                print("Saddlepoint found",currentElement)
            if(row == 5):
                currentElement <= saddleArray[row][col-5] and currentElement <= saddleArray[row][col-4] and currentElement <= saddleArray[row][col-3] and currentElement <= saddleArray[row][col-2] and currentElement <= saddleArray[row][col-1] and currentElement <= saddleArray[row][col-1]
                print("Saddlepoint found",currentElement)
            if(row == 6):
                currentElement <= saddleArray[row][col-6] and currentElement <= saddleArray[row][col-5] and currentElement <= saddleArray[row][col-4] and currentElement <= saddleArray[row][col-3] and currentElement <= saddleArray[row][col-2] and currentElement <= saddleArray[row][col-2]
                print("Saddlepoint found",currentElement)

            col += 1
        row += 1
    
    if(totalSaddlePoints == 0):
        print("There were no saddlepoints found in the array.")

#Execute
main()
