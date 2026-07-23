"""
Program Name : Prime Number Checker
Author       : Neeraj Kaushik

Description:
Check whether a given number is prime or not.
A prime number has exactly two factors:
1 and the number itself.

Example:
Input : 11
Output: 11 is prime

Input : 12
Output: 12 is not prime
"""

# Implementation:

number = int(input("Enter a number: "))

if number == 0 or number == 1:
    print(f"{number} is not prime")

else:
    is_prime = True

    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{number} is prime")
    else:
        print(f"{number} is not prime")