"""
Program Name : Reverse a List
Author       : Neeraj Kaushik
Description  : Reverse a list without using the reverse() method or slicing.

"""

# Implementation:

numbers = [12, 23, 32, 92]
reversed_list = []

last_index = len(numbers) - 1

for i in range(last_index, -1, -1):
    reversed_list.append(numbers[i])

print("Original List :", numbers)
print("Reversed List :", reversed_list)