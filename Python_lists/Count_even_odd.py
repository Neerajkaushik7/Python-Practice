"""
Program Name : Count Even and Odd Numbers in a List
Author       : Neeraj Kaushik

Description:
Count and display the total number of even and odd elements present in a list.

"""

# Implementation:

numbers = [12, 23, 435, 723, 345, 2, 5, 342]

count_even = 0
count_odd = 0

for number in numbers:
    if number % 2 == 0:
        count_even += 1
    else:
        count_odd += 1

print("Total Even Numbers :", count_even)
print("Total Odd Numbers  :", count_odd)