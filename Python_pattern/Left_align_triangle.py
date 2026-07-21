"""
Program Name : Inverted Left-Aligned Right Triangle Pattern
Author       : Neeraj Kaushik

Description:
Print an inverted left-aligned right triangle using the '*' character.
The number of rows is taken as input from the user.

Pattern:
* * * * *
* * * *
* * *
* *
*
"""

# Implementation:

height = int(input("Enter the height: "))

for i in range(1, height + 1):
    for j in range(height - i + 1):
        print("*", end=" ")
    print()