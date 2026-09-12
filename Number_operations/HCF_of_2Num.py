"""
Program Name : HCF of Two Numbers
Author       : Neeraj Kaushik
Description  : Finds the HCF of two numbers using a for loop.
Example Input/Output:
    Input  : 12, 8
    Output : 4
"""

# Function to calculate HCF
def calc_hcf(num1, num2):
    hcf = 1

    for i in range(1, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            hcf = i

    print(hcf)


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

calc_hcf(num1, num2)