"""
Program Name : Remove Duplicates from a List
Author       : Neeraj Kaushik

Description:
Remove duplicate elements from a list without using the set() function.
This program creates a new list containing only unique elements while
preserving their original order.
"""

# Implementation:

data = [8, 12, 3, 27, 41, 3, 22, 99, 12, 10, 70]

unique = []

for number in data:
    if number not in unique:
        unique.append(number)

print(f"Original List : {data}")
print(f"Unique List   : {unique}")