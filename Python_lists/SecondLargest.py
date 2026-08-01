"""
Program Name : Second Largest Number
Author       : Neeraj Kaushik
Description  : Find the second largest number in a list without using sort() or max().

"""

# Implementation:

def findSecLargest(numbers):

    largest = numbers[0]
    secondlargest = 0

    for i in numbers:
        if i > largest:
            secondlargest = largest
            largest = i
        elif i > secondlargest:
            secondlargest = i

    print(f"Largest element is: {largest}")
    print(f"Second Largest element is: {secondlargest}")


numbers = [12, 32, 514, 23, 93, 4]
findSecLargest(numbers)