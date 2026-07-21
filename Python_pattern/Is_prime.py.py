"""
Program Name : Prime Number Checker
Author       : Neeraj Kaushik

Description:
This program checks whether a given number is prime or not.
It uses the optimized approach of checking divisibility only up
to the square root of the number. The program also demonstrates
the use of Python's for-else loop.
"""

# Implementation:

number = int(input("Enter a number to check: "))

if number == 0 or number == 1:
    print(f"{number} is not a prime number.")

else:
    limit = int(number ** 0.5)

    for i in range(2, limit + 1):
        if number % i == 0:
            print(f"{number} is not a prime number.")
            break

    else:
        print(f"{number} is a prime number.")