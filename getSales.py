SIZE = 6

def main():
    getSales()

def getSales():
    sales = []
    counter = 0
    total = 0

    while(len(sales) < SIZE):
        saleInput = float(input("Enter a sale:"))
        sales.append(saleInput)
        
    while(counter < len(sales)):
        total = total + sales[counter]
        counter += 1

    print("The total sales is:",total)

#Execute
main()