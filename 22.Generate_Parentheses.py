# This is the solution of No.22 problem in LeetCode, https://leetcode.com/problems/generate-parentheses/

class Solution(object):
    def generateParenthesis(self, n):
        return self.__gen(2 * n, 0, '')
    def __gen(self, n, sNum, string):
        ret = []
        if n == sNum:
            return [string + ')' * sNum]
        elif n < sNum:
            return None
        if sNum > 0:
            res = self.__gen(n - 1, sNum - 1, string + ')')
            if res != None:
                ret.extend(res)
        res = self.__gen(n - 1, sNum + 1, string + '(')
        if res != None:
            ret.extend(res)
        return ret
