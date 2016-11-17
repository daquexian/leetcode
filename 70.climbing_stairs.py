import sys

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        ans = [1, 2]
        for i in range(2, n):
            ans[0], ans[1] = ans[1], ans[0] + ans[1]
        return ans[1]

n = eval(sys.argv[1])

print Solution().climbStairs(n)
