def main():
    mass = askMass()
    calcAndCompare(mass)

#asks the user for the mass of an object
def askMass():
    askMass = int(input("What is the mass of the object?:"))
    return askMass

#calculates the weight of the object and checks if it's too heavy or too light.
def calcAndCompare(mass):
    weight = mass * 9.8

    if(weight > 1000):
        print("The object is too heavy.")
    else:
        if(weight < 10):
            print("The object is too light.")
    

#Execute
main()