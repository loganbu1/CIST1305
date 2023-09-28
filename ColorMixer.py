def main():
    print("Enter two colors to mix (primary colors only).")
    color1 = askColor1()
    color2 = askColor2()
    checkMixColor(color1,color2)


def askColor1():
    color1 = input(str("Enter color 1:"))
    color1 = color1.lower()
    return color1

def askColor2():
    color2 = input(str("Enter color 2:"))
    color2 = color2.lower()
    return color2

def checkMixColor(color1,color2):
    red = "red"
    blue = "blue"
    yellow = "yellow"
    
    if((color1 == red or color1 == blue or color1 == yellow) and (color2 == red or color2 == blue or color2 == yellow)):
        if(color1 != color2):
            if((color1 == red or color1 == blue) and (color2 == red or color2 == blue)):
                print("The color is purple.")
            else:
                if((color1 == red or color1 == yellow) and (color2 == red or color2 == yellow)):
                    print("The color is orange.")
                else:
                    if((color1 == yellow or color1 == blue) and (color2 == yellow or color2 == blue)):
                        print("The color is green.")      
        else:
            print("ERROR: The colors you input are the same. Please input two different colors.")    
    else:
        print("ERROR: The colors you input are not primary colors.")

#Execute
main()