def main():
    seconds = askSeconds()
    calcMinutes(seconds)
    calcHours(seconds)
    calcDays(seconds)

def askSeconds():
    seconds = int(input("Enter a number of seconds:"))
    return seconds

def calcMinutes(seconds):
    if(seconds >= 60):
        print("Number of minutes:",seconds/60)
    else:
        print("Number of minutes: 0")

def calcHours(seconds):
    if(seconds >= 3600):
        print("Number of hours:",seconds/3600)
    else:
        print("Number of hours: 0")

def calcDays(seconds):
    if(seconds >= 86400):
        print("Number of hours:",seconds/86400)
    else:
        print("Number of days: 0")

#Execute
main()