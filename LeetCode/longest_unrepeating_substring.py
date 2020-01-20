"""
Given a string, find the length of the longest substring without repeating characters.

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

space and time efficiency is O(n) because we only iterate through the
string once.  We also store the items in a dictionary.

"""


def longest_substring_length(s):

    if len(s) == 0:
        return 0

    start = 0
    max_length = 0
    visited = {}

    for i in range(len(s)):
        if s[i] in visited and start <= visited[s[i]]:
            # we found the first match, so we need to restart the start pointer,
            # so it starts from where the previous position of the duplicated character + 1
            start = visited[s[i]] + 1
        else:
            max_length = max(max_length, i - start + 1)
        visited[s[i]] = i

    return max_length


assert longest_substring_length('abcabcbb') == 3
assert longest_substring_length('bbbbb') == 1
assert longest_substring_length('pwwkew') == 3
assert longest_substring_length('') == 0
assert longest_substring_length('a') == 1