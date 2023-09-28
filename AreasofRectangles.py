def main():
    rectangle1W = askRectangle1Width()
    rectangle1H = askRectangle1Height()
    rectangle2W = askRectangle2Width()
    rectangle2H = askRectangle2Height()
    calcAndCompare(rectangle1W, rectangle1H, rectangle2W, rectangle2H)
    

# asks user for width and height for rectangle 1 and returns the variables.
def askRectangle1Width():
    rectangle1Width = int(input("What is the width of rectangle 1?:"))
    return rectangle1Width

def askRectangle1Height():
    rectangle1Height = int(input("What is the height of rectangle 1?:"))
    return rectangle1Height

# asks user for width and height for rectangle 2 and returns the variables.
def askRectangle2Width():
    rectangle2Width = int(input("What is the width of rectangle 2?:"))
    return rectangle2Width

def askRectangle2Height():
    rectangle2Height = int(input("What is the height of rectangle 2?:"))
    return rectangle2Height

#Calculates the areas of the rectangles and compares the areas to see which one has the greater area.
def calcAndCompare(rectangle1W, rectangle1H, rectangle2W, rectangle2H):
    areaRectangle1 = rectangle1W * rectangle1H
    areaRectangle2 = rectangle2W * rectangle2H

    if(areaRectangle1 == areaRectangle2):
        print("The areas of the rectangles are the same.")
    else:
        if(areaRectangle1 > areaRectangle2):
            print("The area of rectangle 1 is greater.")
        else:
            print("The area of rectangle 2 is greater.")
    
#Execute
main()