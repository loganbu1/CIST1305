def main():
    hours = getHours()
    payRate = getPayRate()
    grossPay(payRate,hours)

def getHours():
    hours = int(input("How many hours did you work?"))
    return hours

def getPayRate():
    payRate = int(input("What is your payrate?"))
    return payRate

def grossPay(payRate,grossPay):
    grossPay = payRate * grossPay
    print("Your pay is",grossPay)

#Execute
main()