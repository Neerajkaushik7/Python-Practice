"""
Program Name : LCM of Two Numbers
Author       : Neeraj Kaushik
Description  : This program finds the LCM of two numbers using the HCF logic.
Example Input:
    12
    8
Example Output:
    24.0
"""

# Function to calculate LCM
def calc_lcm(num1,num2):
    orig1=num1
    orig2=num2
    gcd=1

    if(num1<num2):
        temp=num1
        num1=num2
        num2=temp

    while(num2!=0):
        num1=num1%num2
        temp=num1
        num1=num2
        num2=temp

    gcd=num1
    lcm=(orig1*orig2)/gcd
    print(lcm)


num1=12
num2=8

result=calc_lcm(num1,num2)