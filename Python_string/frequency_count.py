"""
Program Name : Character Frequency Counter
Author       : Neeraj Kaushik

Description:
This program counts the frequency of each character
in a given string using a dictionary. It ignores spaces
and treats uppercase and lowercase letters as the same.
"""

# Implementation

sentence = "A brave man".lower()
frequency = {}

for char in sentence:
    if char == ' ':
        continue

    elif char not in frequency:
        frequency[char] = 1

    else:
        frequency[char] += 1

print(frequency)