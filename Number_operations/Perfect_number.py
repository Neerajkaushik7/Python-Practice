"""
Program Name : Perfect Number Checker
Author       : Neeraj Kaushik

Description:
Check whether a given number is a Perfect Number or not.
A Perfect Number is a positive integer that is equal to
the sum of its proper divisors (excluding the number itself).

Example:
6  -> 1 + 2 + 3 = 6  (Perfect Number)
28 -> 1 + 2 + 4 + 7 + 14 = 28 (Perfect Number)
"""

# Implementation:

def is_perfect(number):
    if number <= 1:
        return False

    divisors_sum = 0

    for i in range(1, number):
        if number % i == 0:
            divisors_sum += i

    return divisors_sum == number


number = int(input("Enter a number: "))

if is_perfect(number):
    print(f"{number} is a Perfect Number.")
else:
    print(f"{number} is not a Perfect Number.")