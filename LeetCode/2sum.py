"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
"""

def two_sum(values:list, target:int) -> tuple:
    store = {}

    for i in range(0, len(values)):
        store[values[i]] = i
        needed = target - values[i]
        if needed in store:
            item = store[needed], i
            return item
    return None


assert(two_sum([1, 4, 8, 3, 2, 9, 15], 13)) == (1, 5)
assert(two_sum([2, 7, 11, 15], 9)) == (0, 1)
assert(two_sum([2, 7, 11, 15], 8)) is None
assert(two_sum([2, 7, 11, 15], 26)) == (2, 3)
assert(two_sum([2, 11, -11, 15], 0)) == (1, 2)
