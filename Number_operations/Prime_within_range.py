"""
Program Name : Display Prime Numbers in a Given Range
Author       : Neeraj Kaushik

Description:
Display all prime numbers within a given range.
For each number, indicate whether it is prime or not.

"""

# Implementation:

start = 10
end = 50

# Check each number in the range
for number in range(start, end + 1):


    if number <= 1:
        print(f"{number} is Not Prime")
        continue

    is_prime = True
    for divisor in range(2, number):
        if number % divisor == 0:
            is_prime = False
            break


    if is_prime:
        print(f"{number} is Prime")
    else:
        print(f"{number} is Not Prime")