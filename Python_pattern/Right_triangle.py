"""
Program Name : Left-Aligned Right Triangle Pattern
Author       : Neeraj Kaushik

Description:
Print a left-aligned right triangle using the '*' character.
The number of rows is taken as input from the user.

Pattern:
*
* *
* * *
* * * *
* * * * *
"""

# Implementation:

height = int(input("Enter some value: "))

for i in range(1, height + 1):
    for j in range(i):
        print("*", end=" ")
    print()