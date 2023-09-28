def main():
    weight = askWeight()
    charge = calcCharge(weight)
    printAll(charge)




def askWeight():
    weight = int(input("Enter the weight of the package:"))
    return weight

def calcCharge(weight):
    if(weight <= 2):
        charge = 1.10
    else:
        if(weight > 2 and weight <= 6):
            charge = 2.20
        else:
            if(weight > 6 and weight <= 10):
                charge = 3.70
            else:
                if(weight > 10):
                    charge = 3.80
    return charge

def printAll(charge):
    print("Shipping charge:", "$", charge)

#Execute
main()