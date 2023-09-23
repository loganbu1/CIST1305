def main():
    miles = kilometersToMiles()
    print("In miles:", miles)

def kilometersToMiles():
    kilometers = int(input("What is the distance in kilometers?: "))
    miles = kilometers * 0.6214
    return miles

main()