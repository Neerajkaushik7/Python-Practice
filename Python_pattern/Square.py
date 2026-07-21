"""
Program Name : Square Pattern
Author       : Neeraj Kaushik

Description:
Print a square pattern using the '*' character.
The size of the square is taken as input from the user.

Pattern:
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
"""

# Implementation:

side = int(input("Enter the size: "))

for i in range(1, side + 1):
    for j in range(side):
        print("*", end=" ")
    print()