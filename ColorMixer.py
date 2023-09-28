def main():
    print("Enter two colors to mix (primary colors only).")
    color1 = askColor1()
    color2 = askColor2()
    checkMixColor(color1,color2)


def askColor1():
    color1 = input("Enter color 1:")
    return color1

def askColor2():
    color2 = input("Enter color 2:")
    return color2

def checkMixColor(color1,color2):
    redL = "red"
    redC = "Red"
    blueL = "blue"
    blueC = "Blue"
    yellowL = "yellow"
    yellowC = "Yellow"
    
    #Checks if the user input red, blue, or yellow.
    if(color1 == (redL or redC or blueL or blueC or yellowL or yellowC) and color2 == (redL or redC or blueL or blueC or yellowL or yellowC)):
        #Checks if the two colors are different
        if(color1 != color2):
            #If the colors red and blue are found
            if((color1 or color2 == blueL or blueC) and (color1 or color2 == redL or redC)):
                print("The color is purple.")
            else:
                #If the colors red and yellow are found
                if((color1 or color2 == redL or redC) and (color1 or color2 == yellowL or yellowC)):
                    print("The color is orange.")
                else:
                    #If the colors blue and yellow are found
                    if((color1 or color2 == blueL or blueC) and (color1 or color2 == yellowL or yellowC)):
                        print("The color is green.")
        else:
            print("Error: The colors you input are the same. Please input two different colors.")       
    else:
        print("Error: The only colors that can be mixed are red, blue, or yellow. Please input these colors only.")
    

#Execute
main()