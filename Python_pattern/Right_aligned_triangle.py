"""
Program Name : Right Aligned Triangle Pattern
Author       : Neeraj Kaushik

Description:
Print a right aligned triangle pattern using the '*' character.
The number of rows is taken as input from the user.

Pattern (rows = 5):
        *
      * *
    * * *
  * * * *
* * * * *
"""

# Implementation:

rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):

    # Print leading spaces
    for space in range(rows - i):
        print("", end=" ")

    # Print stars
    for star in range(i):
        print("*", end=" ")

    # Move to the next line
    print()
