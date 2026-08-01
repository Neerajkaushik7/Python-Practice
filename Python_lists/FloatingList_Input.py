"""
Program Name : Input a List of Floating-Point Numbers
Author       : Neeraj Kaushik

Description:
Accept a list of floating-point numbers from the user
and display the entered list.

"""

# Implementation:

# User Input
float_list = list(map(float, input("Enter the floating-point numbers: ").split()))

# Display Result
print("Entered List:", float_list)