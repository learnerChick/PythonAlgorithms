"""
Given an array of positive numbers and a positive number ‘S’,
find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0, if no such subarray exists.

Input: [2, 1, 5, 2, 3, 2], S=7
Output: 2
Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].

Input: [3, 4, 1, 1, 6], S=8
Output: 3
Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6].

Time complexity = O(n)

Space complexity = O(1)

"""

import math

def smallest_subarray_len_for_sum(arr, sum):
    window_start = 0
    smallest = math.inf
    window_sum = 0

    for window_end in range(len(arr)):
        window_sum = window_sum + arr[window_end]
        while window_sum >= sum:
            smallest = min(smallest, window_end - window_start + 1)
            window_sum = window_sum - arr[window_start]
            window_start = window_start + 1

    if smallest == math.inf:
        return 0
    return smallest


assert smallest_subarray_len_for_sum([2, 1, 5, 2, 3, 2], 7) == 2
assert smallest_subarray_len_for_sum([3, 4, 1, 1, 6], 8) == 3
assert smallest_subarray_len_for_sum([2, 1, 5, 2, 8], 7) == 1
