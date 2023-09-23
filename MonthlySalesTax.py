def main():
    tSale = totalSales()
    cTax = countyTax(tSale)
    sTax = stateTax(tSale)
    tSalesTax = totalSalesTax(cTax,sTax)
    printAll(cTax,sTax,tSalesTax)

def totalSales():
    totalSales = int(input("Enter the total sales for the month:"))
    return totalSales

def countyTax(tSale):
    countyTax = tSale * 0.02
    return countyTax

def stateTax(tSale):
    stateTax = tSale * 0.04
    return stateTax

def totalSalesTax(cTax,sTax):
    totalTax = cTax + sTax
    return totalTax

def printAll(cTax,sTax,tSalesTax):
    print("The amount of county sales tax:",cTax)
    print("The amount of state sales tax:",sTax)
    print("The total sales tax:",tSalesTax)
    
#excecute
main()