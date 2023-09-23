

def main():
    price = purchasePrice()
    sTax = stateTax()
    cTax = countyTax()
    tTax = totalTax(sTax,cTax)
    totalSale(tTax,price)


#asks for purchase price and returns it
def purchasePrice():
    purchasePrice = int(input("Enter the amount of the purchase: "))
    print("Purchase price:", purchasePrice)
    return purchasePrice

#displays state tax
def stateTax():
    stateTax = 0.04
    print("State sales tax is:", stateTax)
    return stateTax

#displays county tax
def countyTax():
    countyTax = 0.02
    print("County sales tax is:", countyTax)
    return countyTax

#calculates and displays the total tax
def totalTax(stateTax,countyTax):
    totalTax = stateTax + countyTax
    print("Total sales tax is ", totalTax)
    return totalTax

#calculates the total
def totalSale(totalTax,purchasePrice):
    totalSale = (totalTax * purchasePrice) + purchasePrice
    print("Total:", totalSale)

#excecutes the program
main()

