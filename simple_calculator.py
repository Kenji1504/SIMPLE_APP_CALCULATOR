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
time.sleep(1)
# create a calculator function
def calculator():
    # create a while loop
    while True:
	    # try asking the user to input two numerical values.
        try:
            first_value = float(input("Input the first value: "))
            second_value = float(input("\nInput the second value: "))
            # break the loop if inputs are valid
            break
	    # use except function to capture any Value Error
        except ValueError:
            print("\nInvalid Input, input numerical characters only.\n")
            print("Please try again.\n")
            time.sleep(1)
	
    # ask user for what operator to use
    print("\nInput one of the following values to determine what mathematical operator will be used for calculation.\n")
    time.sleep(1)
    print("Use '+' to indicate addition\nUse '-' to indicate subtraction\
          \nUse 'x' to indicate multiplication\nUse'/' to indicate division")
    time.sleep(1)
    math_operator = input("\nInput what operator to use: ")
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

	# if response '-', subtract the first inputted number to the second inputted number
    elif math_operator == '-':
        print("Here's for the answer:")
        resultant_value = first_value - second_value
        time.sleep(1)
        difference = f"\n{first_value} - {second_value} = {resultant_value}"
        print("\033[1m" + "\033[95m" + pyfiglet.figlet_format(difference.center(65), font= "ntgreek")) 

	# if response is 'x', multiply the first inputted number to the second inputted number
    elif math_operator == 'x':
        print("Here's for the answer:")
        resultant_value = first_value * second_value
        time.sleep(1)
        product = f"\n{first_value} x {second_value} = {resultant_value}"
        print("\033[1m" + "\033[95m" + pyfiglet.figlet_format(product.center(65), font= "ogre"))
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
            # use except function to capture any Zero Division Error
            except ZeroDivisionError:
                print("\nInvalid Input. You're trying to divide a particular number by 0\n")
                print("Please try again.")
            # break the loop
            break
	# else, print Invalid Input

# To loop the program, create a while loop
	# call out the calculator function
	# ask user if they want to try again
		# if response is 'yes', continue
		# if response in 'no', break
		# else 
			# print 'Invalid Input'
			# ask user to try again	
# end program

calculator()