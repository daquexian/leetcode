# This is the solution of No.50 problem in LeetCode, https://leetcode.com/problems/powx-n/

import sys

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        res, tmp = 1, x
        flag = False
        if n < 0:
            flag = True
            n *= -1
        while n > 0:
            if n & 1 == 1:
                res *= tmp
            tmp *= tmp
            n >>= 1
        if flag:
            res = 1. / res
        return res

x = eval(sys.argv[1])
n = eval(sys.argv[2])
print Solution().myPow(x, n)

