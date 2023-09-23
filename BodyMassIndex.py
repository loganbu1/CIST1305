def main():
    weight = getWeight()
    height = getHeight()
    calBMI(weight,height)



def getWeight():
    weight = int(input("What is your weight?:"))
    return weight

def getHeight():
    height = int(input("What is your height?: "))
    return height

def calBMI(weight,height):
    BMI = weight*703/height**2
    print("Your BMI is:", BMI)

#Execute
main()