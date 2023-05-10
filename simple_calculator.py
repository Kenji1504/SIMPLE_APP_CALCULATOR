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
            first_value = float(input("Input the first value: "))
            second_value = float(input("Input the second value: "))
            # break the loop if inputs are valid
            break
	    # use except function to capture any Value Error
        except ValueError:
            print("Invalid Input, input numerical characters only.\n")
            print("Please try again.\n")
	# ask user for what operator to use
	# if response is '+', add two values
	# if response '-', subtract the first inputted number to the second inputted number
	# if response is 'x', multiply the first inputted number to the second inputted number
	# if response is '/' 
        # try dividing the first inputted number to the second inputted number
        # use except function to capture any Zero Division Error
        # break the loop
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