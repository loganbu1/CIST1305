import random

def main():
    A1 = "_"
    A2 = "_"
    A3 = "_"
    B1 = "_"
    B2 = "_"
    B3 = "_"
    C1 = "_"
    C2 = "_"
    C3 = "_"

    print("Welcome to Tic-Tac-Toe!")

    playerShape = decidePlayerShape()
    computerShape = decideComputerShape(playerShape)

    print("To select what cell to place your shape. Use A, B, or C for the columns and 1, 2, or 3 for the rows. For example: If you wanted to select the top left cell you would input: A1")

    drawBoard(A1,A2,A3,B1,B2,B3,C1,C2,C3)

    gameOver = False

    while(gameOver == False):
        #Players turn
        print("Your turn!")

        playTurn = playerTurn()
        cellAvailable = cellAvailability(playTurn,A1,A2,A3,B1,B2,B3,C1,C2,C3)

        while(cellAvailable == False):
            print("ERROR: That cell is already taken, please choose a different spot.")

            playTurn = playerTurn()
            cellAvailable = cellAvailability(playTurn,A1,A2,A3,B1,B2,B3,C1,C2,C3)
        else:
            if(playTurn == "A1"):
                A1 = playerShape
            if(playTurn == "A2"):
                A2 = playerShape
            if(playTurn == "A3"):
                A3 = playerShape
            if(playTurn == "B1"):
                B1 = playerShape
            if(playTurn == "B2"):
                B2 = playerShape
            if(playTurn == "B3"):
                B3 = playerShape
            if(playTurn == "C1"):
                C1 = playerShape
            if(playTurn == "C2"):
                C2 = playerShape
            if(playTurn == "C3"):
                C3 = playerShape
        
        drawBoard(A1,A2,A3,B1,B2,B3,C1,C2,C3)

        #Checks for a win
        winResult = checkWin(A1,A2,A3,B1,B2,B3,C1,C2,C3)

        #Checks for a stalemate
        boardFullResult = checkBoardFull(A1,A2,A3,B1,B2,B3,C1,C2,C3)
        
        if(boardFullResult == True and winResult != True):
            print("There is a tie!")

        #If the game is won or the board is full then the gameOver variable is set to true.
        if(boardFullResult == True or winResult == True):
            gameOver = True
        
        #Skips the computers turn if gameOver is false already. The code will continue if gameOver is still false.
        if(gameOver == False):
            #Computers turn
            compTurn = computerTurn()
            cellAvailable = cellAvailability(playTurn,A1,A2,A3,B1,B2,B3,C1,C2,C3)

            while(cellAvailable == False):
                compTurn = computerTurn()
                cellAvailable = cellAvailability(compTurn,A1,A2,A3,B1,B2,B3,C1,C2,C3)
            else:
                if(compTurn == "A1"):
                    A1 = computerShape
                if(compTurn == "A2"):
                    A2 = computerShape
                if(compTurn == "A3"):
                    A3 = computerShape
                if(compTurn == "B1"):
                    B1 = computerShape
                if(compTurn == "B2"):
                    B2 = computerShape
                if(compTurn == "B3"):
                    B3 = computerShape
                if(compTurn == "C1"):
                    C1 = computerShape
                if(compTurn == "C2"):
                    C2 = computerShape
                if(compTurn == "C3"):
                    C3 = computerShape

            print("The computer choose", compTurn)

            drawBoard(A1,A2,A3,B1,B2,B3,C1,C2,C3)
            
            #Checks for a win
            winResult = checkWin(A1,A2,A3,B1,B2,B3,C1,C2,C3)

            #Checks for a full board
            boardFullResult = checkBoardFull(A1,A2,A3,B1,B2,B3,C1,C2,C3)
            
            if(boardFullResult == True or winResult == True):
                gameOver = True

def decidePlayerShape():
    playerShape = str(input("Do you want to be X or O?:"))

    playerShape = playerShape.upper()

    while(playerShape != "X" and playerShape != "O"):
        print("ERROR: Please enter the letters X or O only. Enter your response again.")

        playerShape = str(input("Do you want to be X or O?:"))
        playerShape = playerShape.upper()
    
    return playerShape

def decideComputerShape(playerShape):
    if(playerShape == "X"):
        computerShape = "O"
    else:
        computerShape = "X"
    
    return computerShape

def playerTurn():
    playTurn = str(input("Enter the cell where you want to place your shape:"))
    
    while(playTurn != "A1" and playTurn != "A2" and playTurn != "A3" and playTurn != "B1" and playTurn != "B2" and playTurn != "B3" and playTurn != "C1" and playTurn != "C2" and playTurn != "C3"):
        print("ERROR: Please input the correct cell location format. Enter your response again.")
        playTurn = str(input("Enter the cell where you want to place your shape:"))
    
    return playTurn
    
def drawBoard(A1,A2,A3,B1,B2,B3,C1,C2,C3):
    print(" ","A","B","C")
    print("1",A1,B1,C1)
    print("2",A2,B2,C2)
    print("3",A3,B3,C3)

def cellAvailability(choice,A1,A2,A3,B1,B2,B3,C1,C2,C3):
    if((choice == "A1" and A1 == "_") or (choice == "A2" and A2 == "_") or (choice == "A3" and A3 == "_") or (choice == "B1" and B1 == "_") or (choice == "B2" and B2 == "_") or (choice == "B3" and B3 == "_") or (choice == "C1" and C1 == "_") or (choice == "C2" and C2 == "_") or (choice == "C3" and C3 == "_")):
        cellAvailable = True
    else:
        cellAvailable = False
        
    return cellAvailable
   
def checkBoardFull(A1,A2,A3,B1,B2,B3,C1,C2,C3):
    if(A1 != "_" and A2 != "_" and A3 != "_" and B1 != "_" and B2 != "_" and B3 != "_" and C1 != "_" and C2 != "_" and C3 != "_"):
        boardFull = True
        return boardFull

def checkWin(A1,A2,A3,B1,B2,B3,C1,C2,C3):
    #Checks if X is the winner
    if(A1 == "X" and B1 == "X" and C1 == "X"):
        print("X wins!")
        win = True
        return win
    if(A2 == "X" and B2 == "X" and C2 == "X"):
        print("X wins!")
        win = True
        return win
    if(A3 == "X" and B3 == "X" and C3 == "X"):
        print("X wins!")
        win = True
        return win
    if(A1 == "X" and A2 == "X" and A3 == "X"):
        print("X wins!")
        win = True
        return win
    if(B1 == "X" and B2 == "X" and B3 == "X"):
        print("X wins!")
        win = True
        return win
    if(C1 == "X" and C2 == "X" and C3 == "X"):
        print("X wins!")
        win = True
        return win
    if(A1 == "X" and B2 == "X" and C3 == "X"):
        print("X wins!")
        win = True
        return win
    if(C1 == "X" and B2 == "X" and A3 == "X"):
        print("X wins!")
        win = True
        return win
    
    #Checks if O is the winner
    if(A1 == "O" and B1 == "O" and C1 == "O"):
        print("O wins!")
        win = True
        return win
    if(A2 == "O" and B2 == "O" and C2 == "O"):
        print("O wins!")
        win = True
        return win
    if(A3 == "O" and B3 == "O" and C3 == "O"):
        print("O wins!")
        win = True
        return win
    if(A1 == "O" and A2 == "O" and A3 == "O"):
        print("O wins!")
        win = True
        return win
    if(B1 == "O" and B2 == "O" and B3 == "O"):
        print("O wins!")
        win = True
        return win
    if(C1 == "O" and C2 == "O" and C3 == "O"):
        print("O wins!")
        win = True
        return win
    if(A1 == "O" and B2 == "O" and C3 == "O"):
        print("O wins!")
        win = True
        return win
    if(C1 == "O" and B2 == "O" and A3 == "O"):
        print("O wins!")
        win = True
        return win
    
def computerTurn():
    A1 = 1
    A2 = 2
    A3 = 3
    B1 = 4
    B2 = 5
    B3 = 6
    C1 = 7
    C2 = 8
    C3 = 9
    
    randomNumber = random.randint(1,9)

    if(randomNumber == 1):
        compChoice = "A1"
    if(randomNumber == 2):
        compChoice = "A2"
    if(randomNumber == 3):
        compChoice = "A3"
    if(randomNumber == 4):
        compChoice = "B1"
    if(randomNumber == 5):
        compChoice = "B2"
    if(randomNumber == 6):
        compChoice = "B3"
    if(randomNumber == 7):
        compChoice = "C1"
    if(randomNumber == 8):
        compChoice = "C2"
    if(randomNumber == 9):
        compChoice = "C3"
    
    return compChoice

#Execute
main()