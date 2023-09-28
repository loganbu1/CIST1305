#Hours,payrate,and gross pay
def main():
    hours = getHours()
    payRate = getPayRate()
    grossPay(payRate,hours)

def getHours():
    hours = float(input("How many hours did you work?"))
    return hours

def getPayRate():
    payRate = float(input("What is your hourly payrate?"))
    return payRate

def grossPay(payRate,grossPay):
    grossPay = payRate * grossPay
    print("Your gross pay is",grossPay)

#Execute
main()
