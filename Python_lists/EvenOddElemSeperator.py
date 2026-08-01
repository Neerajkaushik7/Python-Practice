"""
Program Name : Separate Even and Odd Numbers
Author       : Neeraj Kaushik
Description  : Separate even and odd numbers from a list into two different lists.

"""

# Implementation:

numbers = [12, 421, 43, 13, 153, 12, 52, 1314, 901]

even_list = []
odd_list = []

for i in numbers:
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)

print("Original List :", numbers)
print("Even Numbers  :", even_list)
print("Odd Numbers   :", odd_list)