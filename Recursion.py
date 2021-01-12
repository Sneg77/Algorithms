"""
    Python program for implementation of different types of recursion.
    Time complexity O(n)
"""

def recursive(input):
    if input <= 0:
        return 0
    else:
        output = recursive(input - 1)
        print(output)

def get_fib(position):
    if position == 0 or position == 1:
        return position

    return get_fib(position - 1) + get_fib(position - 2)
