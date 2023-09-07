#N01445323 - Bethany Innes

#function used to calculate the number of gallons needed
def calcPaint(length, width, height, doors, windows):
    
     #gallon equation based on input from user
     gallons = (((2 * (width * height)) + (2 * (length * height))) - ((25 * doors) + (10 * windows))) / 315
     
     return '{gallons: .2f} gallons of paint are needed to paint a room {width: .2f} feet wide\
by {length: .2f} feet long by {height: .2f} feet high with {doors} doors and \
{windows} windows.'.format(**locals())
    
#function used to calulate body mass index and NIH classification
def calcBMI(bodyWeight, bodyHeight):
    
    #BMI equation based on input from user
    bmi = ((bodyWeight * 703) / (bodyHeight * bodyHeight))
    
    bmiClass = ""
    
    #determines users NIH classification based on calculated BMI
    if bmi < 18.5:
        bmiClass = "underweight"      
    elif (bmi >= 18.5) and (bmi <= 24.9):
        bmiClass = "normal"
    elif (bmi >= 25) and (bmi <= 29.9):
        bmiClass = "overweight"
    else:
        bmiClass = "obese"
            
    
    return 'Your BMI is {bmi: .2f}. According to NIH, you are {bmiClass}.'.format(**locals())

#main function
def main():
    
    active = True
    
    #loops until users enters a value other than 1 or 2
    while active:
        print("Welcome to Python program")
        print("Menu options are:")
        print("""
                   Enter 1 for calculating gallons of paint needed to paint a room
                   Enter 2 for calulating Body Mass Index
                   Enter any other value to quit the program""")
   
        option = int(input("Enter menu option: "))         
        
        #exectued if option 1 is selected by user          
        if option == 1:
            while True:
                try:
                    print("Welcome to the paint needed calculator.")
                    rLength = int(input("Enter the length of the room: "))
                    rWidth = int(input("Enter the width of the room: "))
                    rHeight = int(input("Enter the height of the room: "))
                    rDoors =  int(input("How many door are in the room? "))
                    rWindows = int(input("How many windows are in the room? "))
                    
                    #calls paint calulating function
                    paintReport = calcPaint(rLength, rWidth, rHeight, rDoors, rWindows)
                    print(paintReport)
                    print("\n")
                    
                    break 
            
                #executes if user enters anything other than an integer
                except ValueError:
                    print("Atleast one of the values provided is not a number. Please enter valid numbers for all prompts.")
        
           
        #executed if option 2 is selected by user
        elif option == 2:
            while True:
                try:
                    print("Welcome to the body mass index (BMI) calculator.")
                    bodyWeight = int(input("Enter your weight in pounds: "))
                    bodyHeight = int(input("Enter your height in inches: "))
                    
                    
                    #calls BMI calculating function
                    bmiReport = calcBMI(bodyWeight, bodyHeight)
                    print(bmiReport)
                    print("\n")
                    
                    break
                
                #executes if user enters anything other than an integer
                except ValueError:
                    print("Atleast one of the values provided is not a number. Please enter valid numbers for all prompts.")
        
        #will stop the while loop if any other value is entered
        else:
            active = False

#calls main function
main()
                
