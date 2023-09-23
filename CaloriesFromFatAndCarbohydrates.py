def main():
    fat = askFat()
    carbs = askCarbs()
    caloriesFromFat = calFat(fat)
    caloriesFromCarbs = calCarbs(carbs)
    printCalories(caloriesFromFat, caloriesFromCarbs)

def askFat():
    fat = int(input("How many grams of fat have you consumed in the day?:"))
    return fat

def askCarbs():
    carbs = int(input("How many grams of carbohydrates have you consumed in the day?:"))
    return carbs

def calFat(fat):
    calFat = fat * 9
    return calFat

def calCarbs(carbs):
    calCarbs = carbs * 4
    return calCarbs

def printCalories(caloriesFromFat, caloriesFromCarbs):
    print("Your calories from fat are:", caloriesFromFat)
    print("Your calories from carbs are:", caloriesFromCarbs)
    
#execute
main()