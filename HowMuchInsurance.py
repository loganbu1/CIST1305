def main():
    propCost = propertyCost()
    minimumInsurance(propCost)


def propertyCost():
    propertyCost = int(input("How much is replacement the cost of your property?: "))
    return propertyCost

def minimumInsurance(propCost):
    minimumInsurance = propCost * 0.80
    print("The minimum insurance you should buy is:", minimumInsurance)


main()