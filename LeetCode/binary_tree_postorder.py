"""
Given a binary tree, return the postorder traversal of its nodes' values.
(Left, Right, Root)
Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]

For a Graph, the complexity of a Depth First Traversal is O(n + m), where n is the number of nodes, and m is the number of edges.

Since a Binary Tree is also a Graph, the same applies here.
The complexity of each of these Depth-first traversals is O(n+m).

Since the number of edges that can originate from a node is limited to 2 in the case of a Binary Tree,
the maximum number of total edges in a Binary Tree is n-1, where n is the total number of nodes.

The complexity then becomes O(n + n-1), which is O(n).

"""


class Node:
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None


class Solution:
    results = []

    def postorder_traverse(self, root):
        if root is None:
            return

        self.postorder_traverse(root.left)
        self.postorder_traverse(root.right)
        self.results.append(root.val)
        return self.results

# Test
n1 = Node(10)
n2 = Node(5)
n3 = Node(30)
n4 = Node(4)
n5 = Node(8)
n6 = Node(1)
n7 = Node(40)

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5

n3.right = n7
n4.left = n6

assert Solution().postorder_traverse(n1) == [1, 4, 8, 5, 40, 30, 10]



