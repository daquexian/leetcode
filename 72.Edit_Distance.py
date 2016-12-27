import sys


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        len1 = len(word1)
        len2 = len(word2)
        dp = [[i + j for j in range(len2 + 1)] for i in range(len1 + 1)]
        for i in range(0, len1):
            for j in range(0, len2):
                if word1[i] == word2[j]:
                    dp[i + 1][j + 1] = dp[i][j]
                else:
                    dp[i + 1][j + 1] = min(dp[i][j + 1], dp[i + 1][j],
                                           dp[i][j]) + 1
        return dp[-1][-1]

word1 = sys.argv[1]
word2 = sys.argv[2]
print(Solution().minDistance(word1, word2))
