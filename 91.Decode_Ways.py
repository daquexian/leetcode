'''
https://leetcode.com/problems/decode-ways/

A message containing letters from A-Z is being encoded to numbers using the
following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways
to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
'''


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        # dp[i] is num of ways to decode str starting at index i
        dp = [0] * (len(s) + 1)
        dp[-1] = 1
        dp[-2] = 1 if s[-1] != '0' else 0

        i = len(s) - 2
        while i >= 0:
            if s[i] == '1' or (s[i] == '2' and int(s[i + 1]) <= 6):
                dp[i] = dp[i + 1] + dp[i + 2]
            elif s[i] == '0':
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]
            i -= 1
        return dp[0]

s = '111'
print(Solution().numDecodings(s))
