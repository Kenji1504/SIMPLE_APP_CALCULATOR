# Ken Leam G. Gamboa
# BSCPE 1-5
# This program will calculate the two inputted numbers entered
# by the user using the basic mathematical operations.
# Appropriate exception capturing codes will be also implemented in this program.

import time
import pyfiglet

# create program title
PROGRAM_TITLE = "S I M P L E   C A L C U L A T O R"
print("\033[1m" + "\033[95m" + pyfiglet.figlet_format(PROGRAM_TITLE.center(70), font= "short"))
#print short introduction 
# write for an introduction
time.sleep(1)
print("\033[1m" + "\nWelcome to SIMPLE CALCULATOR.") 
time.sleep(1)
print("\nPlease input the following requirements to calculate for the resulting value.\n")

# create a calculator function
def calculator():
    # create a while loop
    while True:
	    # try asking the user to input two numerical values.
        try:
            time.sleep(1)
            first_value = float(input("Input the first value: "))
            time.sleep(1)
            second_value = float(input("\nInput the second value: "))
            # break the loop if inputs are valid
            break
	    # use except function to capture any Value Error
        except ValueError:
            print("\033[31m" + "\nInvalid Input, input numerical characters only.\n")
            print("\033[95m" + "Please try again.\n")
            time.sleep(1)
	
    while True:
        # ask user for what operator to use
        print("\033[95m" + "\nInput one of the following values to determine what mathematical operator will be used for calculation.\n")
        time.sleep(1)
        print("Use '+' to indicate addition\nUse '-' to indicate subtraction\
            \nUse 'x' to indicate multiplication\nUse'/' to indicate division")
        time.sleep(1)
        math_operator = str(input("\nInput what operator to use: "))
        math_operator = math_operator.lower()
        time.sleep(1)
        
        for dot in range(3):
            print(".\n")
            time.sleep(1)
    
        # if response is '+', add two values
        if math_operator == '+':
            print("Here's for the answer:")
            resultant_value = first_value + second_value
            time.sleep(1)
            sum = f"\n{first_value} + {second_value} = {resultant_value}"
            print("\033[1m" + "\033[95m" + pyfiglet.figlet_format(sum.center(65), font= "ntgreek"))
            break

        # if response '-', subtract the first inputted number to the second inputted number
        elif math_operator == '-':
            print("Here's for the answer:")
            resultant_value = first_value - second_value
            time.sleep(1)
            difference = f"\n{first_value} - {second_value} = {resultant_value}"
            print("\033[1m" + "\033[95m" + pyfiglet.figlet_format(difference.center(65), font= "ntgreek"))
            break 

        # if response is 'x', multiply the first inputted number to the second inputted number
        elif math_operator == 'x':
            print("Here's for the answer:")
            resultant_value = first_value * second_value
            time.sleep(1)
            product = f"\n{first_value} x {second_value} = {resultant_value}"
            print("\033[1m" + "\033[95m" + pyfiglet.figlet_format(product.center(65), font= "ogre"))
            break
        # if response is '/' 
        elif math_operator == '/':
            # inside while loop
            while True:
                # try dividing the first inputted number to the second inputted number
                try:
                    resultant_value = first_value / second_value
                    quotient = f"\n{first_value} / {second_value} = {resultant_value}"
                    print("Here's for the answer:")
                    print("\033[1m" + "\033[95m" + pyfiglet.figlet_format(quotient.center(65), font= "ogre"))
                    break
                # use except function to capture any Zero Division Error
                except ZeroDivisionError:
                    print("\033[31m" + "\nInvalid Input. You're trying to divide a particular number by 0\n")
                    print("\033[95m" + "Please try again.")
                    time.sleep(1)
                # break the loop
                break
            break
        # else, print Invalid Input
        else:
            print("\033[31m" + "INVALID INPUT, please try again")

# To loop the program, create a while loop
while True:
    # call out the calculator function
    calculator()
    # ask user if they want to try again
    time.sleep(1)
    while True:
        repeat_program = str(input("\033[95m" + "\nDo you want to try again? (y/n): "))
        repeat_program = repeat_program.lower()
        # if response is 'yes', continue
        if repeat_program == "y":
            continue
        # if response in 'no', break
        elif repeat_program == "n":
            exit()
        else:
            # print 'Invalid Input'
            print("\n\033[31m" + "INVALID INPUT, please try again.")

# end program
