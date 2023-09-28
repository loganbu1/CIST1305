def main():
    month = askMonth()
    day = askDay()
    year = askYear()
    dateChecker(month,day,year)

#asks user for the month, day, and year.
def askMonth():
    month = int(input("Enter the month(in numeric form):"))
    return month

def askDay():
    day = int(input("Enter the day:"))
    return day

def askYear():
    year = int(input("Enter the year(in two-digit form):"))
    return year

#Checks if the date is magic.

def dateChecker(month,day,year):
    if(year == month * day):
        print("The date is magic.")
    else:
        print("The date is not magic.")

#Execute
main()