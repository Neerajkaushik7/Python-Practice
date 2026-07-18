"""
Program Name : Largest number
Author       : Neeraj Kaushik
Description  : Largest number without max method in a list:

"""
#Implementation:

numbers = [21,43, 453, 23, 89]
temp=numbers[0]
for i in numbers:
    if(i>temp):
        temp=i
print(temp)  