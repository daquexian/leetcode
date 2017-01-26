'''
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.
'''


class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False

        '''
        0 for not calculated
        1 for true
        2 for false
        '''
        dp = [[-1] * (len(s2) + 1) for i in range(len(s1) + 1)]
        return self._isInterleave(s1, s2, s3, 0, 0, dp)

    def _isInterleave(self, s1, s2, s3, i, j, dp):
        if len(s3) == i + j and i == len(s1) and j == len(s2):
            return True
        if i <= len(s1) and j <= len(s2) and dp[i][j] != -1:
            return dp[i][j]

        if len(s1) > i and len(s2) > j and s1[i] == s2[j] == s3[i + j]:
            dp[i][j] = self._isInterleave(s1, s2, s3, i + 1, j, dp) \
                        or self._isInterleave(s1, s2, s3, i, j + 1, dp)
        elif len(s1) > i and s1[i] == s3[i + j]:
            dp[i][j] = self._isInterleave(s1, s2, s3, i + 1, j, dp)
        elif len(s2) > j and s2[j] == s3[i + j]:
            dp[i][j] = self._isInterleave(s1, s2, s3, i, j + 1, dp)
        else:
            dp[i][j] = False
        return dp[i][j]


s1, s2, s3 = 'aabcc', 'dbbca', 'aadbbbaccc'
print(Solution().isInterleave(s1, s2, s3))
