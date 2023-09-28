def main():
    weight = getWeight()
    height = getHeight()
    BMI = calBMI(weight,height)
    weightClass(BMI)




def getWeight():
    weight = float(input("What is your weight?:"))
    return weight

def getHeight():
    height = float(input("What is your height?: "))
    return height

def calBMI(weight,height):
    BMI = weight*703/height**2
    print("Your BMI is:", BMI)
    return BMI

def weightClass(BMI):
    if(BMI > 18.5 and BMI < 25):
        print("Your weight is optimal.")
    else:
        if(BMI < 18.5):
            print("You are underweight.")
        else:
            if(BMI > 25):
                print("You are overweight.")
#Execute
main()