"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
"""

def two_sum_indices(values:list, target:int) -> tuple:
    store = {}

    for i in range(0, len(values)):
        store[values[i]] = i
        needed = target - values[i]
        if needed in store:
            item = store[needed], i
            return item
    return None


assert(two_sum_indices([1, 4, 8, 3, 2, 9, 15], 13)) == (1, 5)
assert(two_sum_indices([2, 7, 11, 15], 9)) == (0, 1)
assert(two_sum_indices([2, 7, 11, 15], 8)) is None
assert(two_sum_indices([2, 7, 11, 15], 26)) == (2, 3)
assert(two_sum_indices([2, 11, -11, 15], 0)) == (1, 2)


def two_sum_numbers(values:list, target:int) -> tuple:
    store = {}

    for i in range(0, len(values)):
        store[values[i]] = i
        needed = target - values[i]
        if needed in store:
            item = needed, values[i]
            return item
    return None


assert(two_sum_numbers([1, 4, 8, 3, 2, 9, 15], 13)) == (4, 9)
assert(two_sum_numbers([2, 7, 11, 15], 9)) == (2, 7)
assert(two_sum_numbers([2, 7, 11, 15], 8)) is None
assert(two_sum_numbers([2, 7, 11, 15], 26)) == (11, 15)
assert(two_sum_numbers([2, 11, -11, 15], 0)) == (11, -11)
