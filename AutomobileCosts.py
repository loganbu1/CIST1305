def main():
    Lo = loan()
    Ins = insurance()
    Ga = gas()
    Oi = oil()
    Ti = tires()
    Ma = maintenance()
    printAll(Lo,Ins,Ga,Oi,Ti,Ma)

    totalMonthlyCost = Lo + Ins + Ga + Oi + Ti + Ma
    totalAnnualCost = totalMonthlyCost * 12


def loan():
    loan = int(input("What is your monthly cost for your loan payment?: "))
    return loan

def insurance():
    insurance = int(input("What is your monthly cost for insurance?: "))
    return insurance

def gas():
    gas = int(input("What is your monthly cost for gas?: "))
    return gas

def oil():
    oil = int(input("What is your monthly cost for oil?: "))
    return oil

def tires():
    tires = int(input("What is your monthly cost for tires?: "))
    return tires

def maintenance():
    maintenance = int(input("What is your monthly cost for maintenance: "))
    return maintenance

def printAll(Lo,Ins,Ga,Oi,Ti,Ma):
    print("Your loan cost per month is", Lo)
    print("Your insurance cost per month is", Ins)
    print("Your gas cost per month is", Ga)
    print("Your oil cost per month is:", Oi)
    print("Your tire cost per month is:", Ti)
    print("Your maintenance costs per month are:", Ma)

#excecute
main()