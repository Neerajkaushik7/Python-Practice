"""
Program Name : Reverse a String
Author       : Neeraj Kaushik

Description:
Reverse a string without using slicing or the reversed() function.
"""
#Implementation:

text = "Neeraj Kaushik"
rev = ""

for i in text:
    rev = i + rev

print(rev)