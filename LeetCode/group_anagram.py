"""
Given an array of strings, group anagrams together.

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note:

All inputs will be in lowercase.
The order of your output does not matter.

Time Complexity: O(NK log K)O(NK log K), where N is the length of inp, and K is the maximum length of a string in inp.
The outer loop has complexity O(N) as we iterate through each string. Then, we sort each string in O(K log K) time.

Space Complexity: O(NK), the total information content stored in sorted_list.

"""
import collections


def group_anagram(inp: list) -> list:
    sorted_list = collections.defaultdict(list)

    for word in inp:
        sorted_list[tuple(sorted(word))].append(word)

    print(sorted_list.values())
    return list(sorted_list.values())

assert(group_anagram(["eat", "tea", "tan", "ate", "nat", "bat"]) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']])