'''
Given a binary tree, return the zigzag level order traversal of its nodes'
values. (ie, from left to right, then right to left for the next level and
alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res, thisLevel, nextLevel = [], [], []
        if root is not None:
            nextLevel.append(root)

        leftToRight = False
        while len(nextLevel) > 0:
            thisLevel, nextLevel = nextLevel, []
            if leftToRight:
                for node in reversed(thisLevel):
                    if node.left is not None:
                        nextLevel.append(node.left)
                    if node.right is not None:
                        nextLevel.append(node.right)
            else:
                for node in reversed(thisLevel):
                    if node.right is not None:
                        nextLevel.append(node.right)
                    if node.left is not None:
                        nextLevel.append(node.left)
            res.append([x.val for x in thisLevel])
            leftToRight = not leftToRight

        return res
