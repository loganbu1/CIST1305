def main():
    pPrice = propPrice()
    aValue = assesmentValue(pPrice)
    pTax = propertyTax(aValue)
    printAll(aValue,pTax)



def propPrice():
    propertyPrice = int(input("What is the actual value of your property?:"))
    return propertyPrice

def assesmentValue(pPrice):
    assesmentValue = pPrice * 0.60
    return assesmentValue

def propertyTax(aValue):
    propertyTax = ((aValue / 100)*0.64)
    return propertyTax


def printAll(aValue,pTax):
    print("The assesment value of your property is:", aValue)
    print("The property tax is:", pTax)
main()

