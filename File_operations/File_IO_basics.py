"""
Program Name : Basic File Handling
Author       : Neeraj Kaushik

Description:
Demonstrate basic file handling operations in Python:
write, read, append, and automatic file closing.

Operations:
1. Write data to a file
2. Read data from a file
3. Append new data to the file
4. Read the updated file

File Used: demo.txt
"""

# Basic File Handling

# Write data to the file
with open("demo.txt", "w") as file:
    file.write("Hello Python\n")
    file.write("Learning file handling in Python.\n")


# Read data from the file
with open("demo.txt", "r") as file:
    print("File content:")
    print(file.read())


# Append new data to the file
with open("demo.txt", "a") as file:
    file.write("New line added using append mode.\n")


# Read the updated file
with open("demo.txt", "r") as file:
    print("Updated file content:")
    print(file.read())