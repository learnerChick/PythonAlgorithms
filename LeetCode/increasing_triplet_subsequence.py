"""
Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:

Return true if there exists i, j, k
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.

Example 1:
Input: [1,2,3,4,5]
Output: true

Example 2:
Input: [5,4,3,2,1]
Output: false
"""


def increasing_triplet_subsequence(items):
    min_one = None
    min_two = None

    for number in items:
        if min_one is None or min_one >= number:
            min_one = number
        elif min_two is None or min_two >= number:
            min_two = number
        else:
            return True

    return False


assert increasing_triplet_subsequence([1, 2, 3, 4, 5]) is True
assert increasing_triplet_subsequence([5, 4, 3, 2, 1]) is False