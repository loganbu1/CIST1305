import math

def main():
    numPeople = askNumPeople()
    numHotdogPer = askNumberOfHotdogsPer()
    minPackDogs = minimumPackagesDogs(numPeople,numHotdogPer)
    minPackBuns = minimumPackagesBuns(numPeople,numHotdogPer)
    hotdogsLeft = hotdogsLeftover(numPeople,numHotdogPer,minPackDogs)
    bunsLeft = bunsLeftover(numPeople,numHotdogPer,minPackBuns)
    printAll(minPackDogs,minPackBuns,hotdogsLeft,bunsLeft)

def askNumPeople():
    numPeople = int(input("How many people are attending the cookout?:"))
    return numPeople

def askNumberOfHotdogsPer():
    numberOfHotdogsPer = int(input("How many hotdogs with each person get?:"))
    return numberOfHotdogsPer

def minimumPackagesDogs(numPeople,numHotdogPer):
    minimumPackagesDogs = (numPeople * numHotdogPer)/10
    minimumPackagesDogs = math.ceil(minimumPackagesDogs)
    return minimumPackagesDogs

def minimumPackagesBuns(numPeople,numHotdogPer):
    minimumPackagesBuns = (numPeople * numHotdogPer)/8
    minimumPackagesBuns = math.ceil(minimumPackagesBuns)
    return minimumPackagesBuns

def hotdogsLeftover(numPeople,numHotdogPer,minPackDogs):
    hotdogsLeftover = (minPackDogs * 10) - (numPeople * numHotdogPer)
    return hotdogsLeftover

def bunsLeftover(numPeople,numHotdogPer,minPackBuns):
    bunsLeft = (minPackBuns * 8) - (numPeople * numHotdogPer)
    return bunsLeft

def printAll(minPackDogs,minPackBuns,hotdogsLeft,bunsLeft):
    print("The minimum number of packages of hot dogs required (rounded up to prevent decimel):",minPackDogs)
    print("The minimum number of packages of buns required(rounded up to prevent decimel):",minPackBuns)
    print("The number of hot dogs that will be left over:",hotdogsLeft)
    print("The number of buns that will be left over:",bunsLeft)

#excecute
main()