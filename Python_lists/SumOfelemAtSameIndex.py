"""
Program Name : Sum Corresponding Elements of Two Lists
Author       : Neeraj Kaushik

Description:
Accept two lists from the user and add the corresponding elements.
If one list is longer than the other, append the remaining elements
to the result and display the final list.

"""

# Implementation:

def list_sum(a, b):
    result = []
    common = min(len(a), len(b))

    # Add corresponding elements
    for i in range(common):
        result.append(a[i] + b[i])

    # Append remaining elements from the longer list
    if len(a) > len(b):
        for i in range(common, len(a)):
            result.append(a[i])
    else:
        for i in range(common, len(b)):
            result.append(b[i])

    return result


# User Input
list1 = list(map(int, input("Enter the first list: ").split()))
list2 = list(map(int, input("Enter the second list: ").split()))

# Display Result
print("Resultant List:", list_sum(list1, list2))