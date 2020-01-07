"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = n?
Find all unique triplets in the array which gives the sum of n.

Note:

The solution set must not contain duplicate triplets.
Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

Complexity = O(n^2)
"""


# sort the number so that we can have 2 pointers
def three_sum(numbers: list, target) -> list:
    numbers.sort()

    results = []
    # We do not need to try the last two, since there are no rooms for l and r pointers
    for i in range(0, len(numbers)-2):

        # if the number is the same as the number before, we have used it as target already, continue.
        if i > 0 and numbers[i] == numbers[i-1]:
            continue

        left, right = i+1, len(numbers) - 1

        while left < right:
            total = numbers[i] + numbers[left] + numbers[right]

            # If the total is less than zero, we need it to be larger, so we move the left pointer.
            if total < target:
                left = left + 1
            # If the total is more than zero, we need it to be smaller, so we move the right pointer.
            elif total > target:
                right = right - 1
            else:
                results.append([numbers[i], numbers[left], numbers[right]])
                while left < right and numbers[left] == numbers[left + 1]:
                    left = left + 1
                while left < right and numbers[right] == numbers[right-1]:
                    right = right - 1

                left = left + 1
                right = right - 1

    return results


assert(three_sum([-1, 0, 1, 2, -1, -4], -6)) == [[-4, -1, -1]]
assert(three_sum([-1, 0, 1, 2, -1, -4], 0)) == [[-1, -1, 2], [-1, 0, 1]]
assert(three_sum([1, 4, 45, 6, 10, 8, 12], 22)) == [[4, 6, 12], [4, 8, 10]]
assert(three_sum([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6], 0)) == [[-4, -2, 6], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2], [-2, -2, 4], [-2, 0, 2]]


