menuSelection = 0
inches = 0
centimeters = 0
feet = 0
meters = 0
miles = 0
kilometers = 0

def main():
    print("1. Convert inches to centimeters")
    print("2. Convert feet to meters")
    print("3. Convert miles to kilometers")

    menuSelection = int(input("Enter your selection:"))
    menu(menuSelection)

def inchesToCentimeters():
    inches = float(input("Enter the amount of inches:"))
    centimeters = inches * 2.54
    print(inches,"inches in centimeters is:",centimeters,"centimeters.")

def feetToMeters():
    feet = float(input("Enter the amount of feet:"))
    meters = feet * 0.3048
    print(feet,"feet in meters is:",meters,"meters.")

def milesToKilometers():
    miles = float(input("Enter the amount of miles:"))
    kilometers = miles * 1.609
    print(miles,"miles in kilometers is:",kilometers,"kilometers.")

def menu(menuSelection):
    if(menuSelection == 1 or menuSelection == 2 or menuSelection == 3):
        if(menuSelection == 1):
            inchesToCentimeters()
        elif(menuSelection == 2):
            feetToMeters()
        elif(menuSelection == 3):
            milesToKilometers()
    else:
        print("ERROR: Input was not one of the availible options. Please reinput your answer.")
        menuSelection = int(input("Enter your selection:"))
        menu(menuSelection)

#Execute
main()
