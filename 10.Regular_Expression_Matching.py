# This is the solution of No.10 problem in LeetCode, https://leetcode.com/problems/regular-expression-matching/
# Must use dp.
# I'm inspried by https://leetcode.com/discuss/18970/concise-recursive-and-dp-solutions-with-full-explanation-in
# I will think this problem again tomorrow.

import sys

class Solution(object):
    def isMatch(self, s, p):
        dp = [[False for col in range(len(p) + 1)] for row in range(len(s) + 1)]
        dp[0][0] = True
        j = 2
        while(j <= len(p)):
            if p[j - 1] == '*' and dp[0][j - 2] == True:
                dp[0][j] = True
            else:
                break
            j += 2
        i, j = 1, 1
        while i <= len(s):
            j = min(i, 2)
            while j <= len(p):
                if dp[i - 1][j - 1] == True and (s[i-1] == p[j-1] or p[j-1] == '.'): 
                    dp[i][j] = True
                elif p[j-1] == '*':
                    if dp[i][j - 2] == True:
                        dp[i][j] = True
                    elif dp[i - 1][j - 2] == True and (p[j-2] == s[i-1] or p[j-2] == '.'):
                        dp[i][j] = True
                    elif dp[i - 1][j] == True and (p[j-2] == s[i-1] or p[j-2] == '.'):
                        dp[i][j] = True
                j += 1
            i += 1
        return dp[len(s)][len(p)]

s = sys.argv[1]
p = sys.argv[2]
print 's=', len(s), 'p=', len(p)


print Solution().isMatch(s, p)
