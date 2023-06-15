"""
Find the greatest single number in an array, with runtime of O(n)
"""

def greatest_number(arr):
    max = 0
    for num in arr:
        if num > max:
            max = num
    return max

arr = [1, 100, 34, 50, 99]

assert greatest_number(arr) == 100