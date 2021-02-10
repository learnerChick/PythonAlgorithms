"""

Given an array of positive numbers and a positive number "k",
find the maximum sum of any contiguous subarray of size "k".

Time complexity = O(n)

Space complexity = O(1)
"""

def max_sum_subarray_size_k(arr, k):
    window_start = 0
    window_sum = 0
    maximum_sum = 0

    for window_end in range(len(arr)):
        window_sum = window_sum + arr[window_end]
        if window_end >= k-1:
            maximum_sum = max(window_sum, maximum_sum)
            window_sum = window_sum - arr[window_start]
            window_start = window_start + 1
    return maximum_sum


assert max_sum_subarray_size_k([2, 1, 5, 1, 3, 2], 3) == 9
assert max_sum_subarray_size_k([2, 3, 4, 1, 5], 2) == 7
