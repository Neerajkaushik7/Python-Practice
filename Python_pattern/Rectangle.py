"""
Program Name : Rectangle Pattern
Author       : Neeraj Kaushik

Description:
Print a rectangle pattern using the '*' character.
The length and breadth of the rectangle are taken as input from the user.

Pattern:
* * * * *
* * * * *
* * * * *
"""

# Implementation:

length = int(input("Enter length of rectangle: "))
breadth = int(input("Enter breadth of rectangle: "))

for i in range(1, length + 1):
    for j in range(breadth):
        print("*", end=" ")
    print()