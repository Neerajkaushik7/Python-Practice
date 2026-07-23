"""
Program Name : Reverse a Number
Author       : Neeraj Kaushik

Description:
Reverse a given number using arithmetic operations.
The number is taken as input from the user.

Example:
Input : 357
Output: 753
"""

# Implementation:

number = int(input("Enter a number: "))
reverse = 0

while number != 0:
    last_digit = number % 10
    reverse = (reverse * 10) + last_digit
    number = number // 10

print(f"Reversed number: {reverse}")