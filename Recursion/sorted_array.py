"""
Given an array, find out if the array is sorted using recursion.

Time complexity: O(n)
Space complexity: O(n)
"""

def is_sorted(lst):
    if len(lst) <= 1:
        return True
    else:
        if lst[0] < lst[1]:
            return is_sorted(lst[1:])
        else:
            return False

    return True


assert(is_sorted([1,2,3,4,5]) == True)
assert(is_sorted([3])) == True
assert(is_sorted([])) == True
assert(is_sorted([3,2,4])) == False