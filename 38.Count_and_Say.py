# This is the solution of No.38 problem in LeetCode, https://leetcode.com/problems/count-and-say/

import sys

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        t = '1'
        for i in range(n - 1):
            prev = ''
            r = ''
            for x in t:
                if prev != '':
                    if x == prev:
                        num += 1
                    else:
                        r += (str(num) + prev)
                        prev = x
                        num = 1
                else:
                    prev = x
                    num = 1
            r += (str(num) + prev)
            t = r
        return t

n = eval(sys.argv[1])
print Solution().countAndSay(n)
