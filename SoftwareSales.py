def main():
    packages = askPackages()
    discount = calcPrice(packages)
    percent = calculatePercent(discount)
    printTotal(packages,discount,percent)


def askPackages():
    packages = int(input("How many packages did you purchase?:"))
    return packages

def calcPrice(packages):
    discount = 0
    noDiscount = 404

    #Calculates a discount if the packages are greater than or equal to 10, otherwise the code will return the noDiscount variable
    if(packages >= 10):
        if(packages >= 10 and packages <= 19):
            discount = 0.20
            return discount
        if(packages >= 20 and packages <= 49):
            discount = 0.30
            return discount
        if(packages >= 50 and packages <= 99):
            discount = 0.40
            return discount
        if(packages >= 100):
            discount = 0.50
            return discount
    else:
        return noDiscount


def calculatePercent(discount):
        #If discount is found to be 404 (or not eligible for a discount) this code will be skipped
        if(discount != 404):
            if(discount == 0.20):
                percent = "20% off"
                return percent
            if(discount == 0.30):
                percent = "30% off"
                return percent
            if(discount == 0.40):
                percent = "40% off"
                return percent
            if(discount == 0.50):
                percent = "50% off"
                return percent

def printTotal(packages,discount,percent):
    total = packages * 99

    #If discount is found to be 404 (or not eligible for a discount) the discount code will not be calculated
    if(discount != 404):
        totalWithDiscount = total - (total * discount)

    #Determines if the total is printing with or without a discount.
    if(discount != 404):
        print("Amount of the discount:", percent)
        print("Total amount of purchase:", totalWithDiscount)
    else:
        print("Total amount of purchase:", total)

#Execute
main()