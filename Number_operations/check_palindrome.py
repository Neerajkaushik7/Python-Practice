"""
Program Name : Palindrome Number Checker
Author       : Neeraj Kaushik

Description:
Check whether a given number is a palindrome.
A palindrome number remains the same when its digits are reversed.

Example:
Input : 1221
Output: The number 1221 is a palindrome.

"""

# Implementation:

number = int(input("Enter a number: "))
check_pal = number
reverse = 0

while check_pal != 0:
    last_digit = check_pal % 10
    reverse = (reverse * 10) + last_digit
    check_pal = check_pal // 10

print(f"Reversed number: {reverse}")

if number == reverse:
    print(f"The number {number} is a palindrome.")
else:
    print(f"The number {number} is not a palindrome.")