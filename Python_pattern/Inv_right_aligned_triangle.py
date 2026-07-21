"""
Program Name : Inverted Right-Aligned Right Triangle Pattern
Author       : Neeraj Kaushik

Description:
Print an inverted right-aligned right triangle using the '*' character.
The number of rows is taken as input from the user.

Pattern:
*****
 ****
  ***
   **
    *
"""

# Implementation:

number = int(input("Enter the height: "))

for i in range(1, number + 1):
    for space in range(i):
        print(" ", end="")

    for star in range(number - i + 1):
        print("*", end="")

    print()