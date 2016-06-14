# This is the solution of No.20 problem in LeetCode, https://leetcode.com/problems/valid-parentheses/

class Solution(object):
    def isValid(self, s):
        stack = []
        dic = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if c not in dic:
                stack.append(c)
            else:
                if len(stack) == 0 or stack[-1] != dic[c]:
                    return False
                else:
                    stack.pop()
        if len(stack) != 0:
            return False
        return True
