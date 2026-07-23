"""
Program Name : Fibonacci Series
Author       : Neeraj Kaushik

Description:
Generate the Fibonacci series up to the specified number of terms.
Each number in the series is the sum of the two preceding numbers.

Example:
Input : 10
Output: 0 1 1 2 3 5 8 13 21 34
"""

# Fibonacci Series

number = int(input("Enter the number of terms: "))

first = 0
second = 1

for i in range(number):
    print(first, end=" ")
    next = first + second
    first = second
    second = next