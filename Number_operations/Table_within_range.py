"""
Program Name : Multiplication Table in Range
Author       : Neeraj Kaushik

Description:
Generate multiplication tables for all numbers within the
specified range. The tables are displayed side by side.

Example:
Input :
3
6

Output:
3 * 1 = 3    4 * 1 = 4    5 * 1 = 5    6 * 1 = 6
3 * 2 = 6    4 * 2 = 8    5 * 2 = 10   6 * 2 = 12
"""

# Multiplication Table in Range

number1=int(input())
number2=int(input())

for i in range(1,11):
    for j in range(number1,number2+1):
        print(j,"*",i,"=",j*i,end="\t")
    print()