def main():
    print("Enter the number of coins required to make exactly one doller.")
    pennies = askPennies()
    nickels = askNickels()
    dimes = askDimes()
    quaters = askQuaters()
    calcWin(pennies,nickels,dimes,quaters)

def askPennies():
    pennies = int(input("How many pennies?:"))
    pennies = pennies * 0.01
    return pennies

def askNickels():
    nickels = int(input("How many nickels?:"))
    nickels = nickels * 0.05
    return nickels

def askDimes():
    dimes = int(input("How many dimes?:"))
    dimes = dimes * 0.10
    return dimes

def askQuaters():
    quaters = int(input("How many quaters?:"))
    quaters = quaters * 0.25
    return quaters

def calcWin(pennies,nickels,dimes,quaters):
    total = pennies + nickels + dimes + quaters

    if(total == 1):
        print("Congrats! You made exactly one dollar")
    else:
        print("Sorry! That is not one dollar.")

#Execute
main()