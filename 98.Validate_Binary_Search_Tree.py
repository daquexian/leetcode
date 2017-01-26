'''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's
key.
The right subtree of a node contains only nodes with keys greater than the
node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:
    2
   / \
  1   3
Binary tree [2,1,3], return true.
Example 2:
    1
   / \
  2   3
Binary tree [1,2,3], return false.
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        inorder = self.inorderTraversal(root)
        for i in range(len(inorder) - 1):
            if inorder[i] >= inorder[i + 1]:
                return False
        return True

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        s, n, res = [], root, []
        while True:
            while n is not None:
                s.append(n)
                n = n.left
            while len(s) > 0:
                n = s.pop()
                res.append(n.val)
                if n.right is not None:
                    n = n.right
                    break
            else:
                break
        return res
