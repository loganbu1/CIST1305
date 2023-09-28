def main():
    year = askYear()
    calcLeapYear(year)

def askYear():
    year = int(input("Enter a year:"))
    return year

def calcLeapYear(year):
    if(year % 100 == 0 and year % 400 == 0):
        print("This year is a leap year.")
    else:
        if(year % 100 > 0 and year % 4 == 0):
            print("This year is a leap year.")
        else:
            print("This year is not a leap year.")

#Execute
main()