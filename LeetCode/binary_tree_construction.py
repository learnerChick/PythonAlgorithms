"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7

"""


class Node:
    def __init__(self, v):
        self.left = None
        self.right = None
        self.val = v

class Solution:
    def build_tree(self, preorder: list, inorder: list) -> Node:
        if preorder == [] or inorder == []:
            return None

        # preorder traversal -> Root, Left, Right.  So, we know the root will be the
        # first item in the preordered list.
        root = Node(preorder[0])

        # In the inordered index, items left to the root will be in the left subtree,
        # items to the right will be in the right subtree.
        index = inorder.index(preorder[0])

        root.left = self.build_tree(preorder[1:index+1], inorder[:index])
        root.right = self.build_tree(preorder[index+1:], inorder[index+1:])
        return root


def equals(tree_one: Node, tree_two: Node) -> bool:
    if tree_one == tree_two:
        return True

    if tree_one is None or tree_two is None:
        return False

    return tree_one.val == tree_two.val and \
           equals(tree_one.left, tree_two.left) and \
           equals(tree_one.right, tree_two.right)


three = Node(3)
nine = Node(9)
twenty = Node(20)
fifteen = Node(15)
seven = Node(7)
three.left = nine
three.right = twenty
twenty.left = fifteen
twenty.right = seven

assert equals(Solution().build_tree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]), three)




