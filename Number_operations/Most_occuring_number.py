"""
Program Name : Find Most Occurring Number
Author       : Neeraj Kaushik

Description  :
Find the number that occurs the most frequently in a given list
using a dictionary and loops.

Example:
Input  : [12, 33, 53, 13, 11, 33, 53, 13, 13]
Output : Most occurring number is 13 and it occurred 3 times
"""

# Find Most Occurring Number

# Input list
list2 = [12, 33, 53, 13, 11, 33, 53, 13, 13]

# Create dictionary to store frequency of each number
dic = {}

for i in list2:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] = dic[i] + 1

print(dic)

# Find the number with maximum frequency
x = next(iter(dic.values()))
main_key = None

for key, value in dic.items():
    if x < value:
        x = value
        main_key = key

# Display result
print(f"Most occurring number is {main_key} and it occured {x} times")


# Example Output:
# {12: 1, 33: 2, 53: 2, 13: 3, 11: 1}
# Most occurring number is 13 and it occured 3 times