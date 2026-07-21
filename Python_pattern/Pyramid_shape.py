"""
Program Name : Full Pyramid Pattern
Author       : Neeraj Kaushik

Description:
Print a full pyramid using the '*' character.
The number of rows is taken as input from the user.

Pattern:
    *
   ***
  *****
 *******
*********
"""

# Implementation:

number = int(input("Enter the height: "))

for i in range(1, number + 1):
    for space in range(number - i):
        print(" ", end="")

    for star in range(2 * i - 1):
        print("*", end="")

    print()