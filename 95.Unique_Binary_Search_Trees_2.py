'''
Given an integer n, generate all structurally unique BST's (binary search trees)
that store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self._generateTrees(1, n + 1)

    def _generateTrees(self, l, h):  # [l, h)
        if l == h:
            return [None]
        res = []
        for i in range(l, h):
            tmp1 = self._generateTrees(l, i)
            tmp2 = self._generateTrees(i + 1, h)
            for node1 in tmp1:
                for node2 in tmp2:
                    node = TreeNode(i)
                    node.left = node1
                    node.right = node2
                    res.append(node)
        return res
