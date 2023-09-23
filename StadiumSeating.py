def main():
    tixA = classA()
    tixB = classB()
    tixC = classC()
    ticketSales(tixA,tixB,tixC)

def classA():
    classA = int(input("How many seats were sold for Class A?:"))
    return classA

def classB():
    classB = int(input("How many seats were sold for Class B?:"))
    return classB
    
def classC():
    classC = int(input("How many seats were sold for Class C?:"))
    return classC

def ticketSales(tixA,tixB,tixC):
    ticketSales = (tixA * 15) + (tixB * 12) + (tixC * 9)
    print("The total income generated for this game in dollars was:", ticketSales )



#excute
main()