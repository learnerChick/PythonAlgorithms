"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

Time Complexity: O(m + n) where m and n are number of nodes in first and second lists respectively.

"""


class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


def add_two_numbers(list_one:Node, list_two:Node)-> Node:
    list_sum = None
    list_head = None
    carryover = 0

    while list_one or list_two:
        total = (list_one.val if list_one else 0) + (list_two.val if list_two else 0)
        sum = total + carryover

        if sum >= 10:
            carryover = 1
            remainder = sum % 10
        else:
            carryover = 0
            remainder = sum

        if list_sum is None:
            list_sum = Node(remainder)
            list_head = list_sum
        else:
            list_sum.next = Node(remainder)
            list_sum = list_sum.next

        if list_one:
            list_one = list_one.next
        if list_two:
            list_two = list_two.next

    if carryover > 0:
        list_sum.next = Node(carryover)
    return list_head


def print_linked_list(node):
    items = []
    while node:
        items.append(node.val)
        node = node.next
    return items


def create_linked_list(items):
    head = None
    root = None
    for item in items:
        if head is None:
            head = Node(item)
            root = head
        else:
            head.next = Node(item)
            head = head.next
    return root


assert print_linked_list(add_two_numbers(create_linked_list([2, 4, 3]), create_linked_list([5, 6, 4]))) == [7, 0, 8]
assert print_linked_list(add_two_numbers(create_linked_list([7, 5, 9, 4, 6]), create_linked_list([8, 4]))) == [5, 0, 0, 5, 6]
assert print_linked_list(add_two_numbers(create_linked_list([9, 3]), create_linked_list([1, 6]))) == [0, 0, 1]
