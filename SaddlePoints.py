SIZE = 7
import random
def main():
    saddleArray =[[0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0],]

    row = 0
    while row < SIZE:
        col = 0
        while(col < SIZE):
            saddleArray[row][col] = random.randint(1,10)
            col += 1
        row += 1
    
    row = 0
    while row < SIZE:
        col = 0
        while(col < SIZE):
            print(saddleArray[row][col])
            col += 1
        row += 1
    
#Execute
main()