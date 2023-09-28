def main():
   inputValue = checkRange()
   convert(inputValue)


# Checks if the user inputted number is within 1-10. If the number isn't within the range it will return an error code (the number 404).
def checkRange():
    num = int(input("Input a number within the range of 1 through 10:"))
    error = 404
    
    if(num >= 1 and num <= 10):
        return num
    else:
        return error

# Checks if the range code returns an error
# and displays an error if one is found. If the there is no error then the code 
# will run the Roman numeral converter and the result printer
def convert(inputValue):
    if(inputValue == 404):
       print("Error: The number you input is not within the range.")
    else:
       result = romanNumConverter(inputValue)
       printAll(inputValue,result)

# Converts the user input into a Roman numeral
def romanNumConverter(inputValue):

    I = 1
    II = 2
    III = 3
    IV = 4
    V = 5
    VI = 6
    VII = 7
    VIII = 8
    IX = 9
    X = 10
    
    if(inputValue == I):
        I = "I"
        return I
    else: 
        if(inputValue == II):
            II = "II"
            return II
        else:
            if(inputValue == III):
                III = "III"
                return III
            else:
                if(inputValue == IV):
                    IV = "IV"
                    return IV
                else:
                    if(inputValue == V):
                        V = "V"
                        return V
                    else:
                        if(inputValue == VI):
                            VI = "VI"
                            return VI
                        else:
                            if(inputValue == VII):
                                VII = "VII"
                                return VII
                            else:
                                if(inputValue == VIII):
                                    VIII = "VIII"
                                    return VIII
                                else:
                                    if(inputValue == IX):
                                        IX = "IX"
                                        return IX
                                    else:
                                        if(inputValue == X):
                                            X = "X"
                                            return X
# Prints the result
def printAll(inputValue,result):
    print("The number",inputValue,"converted to a Roman numeral is:",result)



#excecute
main()