def main():
    squareFeet = askSquareFeet()
    pricePaint = askPricePaint()
    galRequired = gallonsNeeded(squareFeet)
    labRequired = laborRequired(squareFeet)
    pCost = paintCost(pricePaint,galRequired)
    lCost = laborCost(labRequired)
    tCost = totalCost(pCost,lCost)
    printAll(galRequired,labRequired,pCost,lCost,tCost)

def askSquareFeet():
    squareFeet = int(input("Enter the square feet of wall space to be painted:"))
    return squareFeet

def askPricePaint():
    pricePaint = int(input("What is the price of the paint per gallon?:"))
    return pricePaint

def gallonsNeeded(squareFeet):
    gallonsNeeded = squareFeet/115
    return gallonsNeeded

def laborRequired(squareFeet):
    laborRequired = (squareFeet/115)*8
    return laborRequired

def paintCost(pricePaint,galRequired):
    paintCost = pricePaint * galRequired
    return paintCost

def laborCost(labRequired):
    laborCost = labRequired * 20
    return laborCost

def totalCost(pCost,lCost):
    totalCost = pCost + lCost
    return totalCost

def printAll(galRequired,labRequired,pCost,lCost,tCost):
    print("The number of gallons of paint required:",galRequired)
    print("The hours of labor required:",labRequired)
    print("The cost of the paint",pCost)
    print("The cost of the labor:",lCost)
    print("The total cost of the paint job:", tCost)
#execute
main()