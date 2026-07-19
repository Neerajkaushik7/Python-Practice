"""
Program Name : Count Vowels in a String
Author       : Neeraj Kaushik

Description:
Find and display all vowels present in a string along with their index positions
using the enumerate() function.
"""

# Implementation:

name = "Neeraj"

for index, i in enumerate(name):
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        print(f"Vowel found at index {index} and it is '{i}'")