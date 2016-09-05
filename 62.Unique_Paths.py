# intelligent solution, proud of myself

import sys

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [1] * n
        for i in range(1, m):
            for j in range(n):
                dp[j] += dp[j - 1] if j > 0 else 0
        return dp[-1]

m = eval(sys.argv[1])
n = eval(sys.argv[2])
print Solution().uniquePaths(m, n)
