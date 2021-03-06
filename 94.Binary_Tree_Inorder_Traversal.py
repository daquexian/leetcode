'''
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],
   1
    \
     2
    /
   3
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
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
