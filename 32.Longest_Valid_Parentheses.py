# This is the solution of No.32 problem in LeetCode, https://leetcode.com/problems/longest-valid-parentheses/

import sys

class Solution:
    def longest(self, s):
        if len(s) == 0:
            return 0
        pos = []
        res = [0] * len(s)
        for i in range(len(s)):
#            print res
            if s[i] == '(':
                pos.append(i)
            elif s[i] == ')':
                if len(pos) == 0:
                    res[i] = 0
                else:
                    top_pos = pos.pop()
                    if top_pos == 0:
                        res[i] = i + 1
                    else:
                        res[i] = res[top_pos - 1] + (i - top_pos + 1)
                    #if s[i - 1] == '(':
                    #    res[i] = 2 if i == 1 else res[i - 2] + 2
                    #elif s[i - 1] == ')':
                    #    res[i] = res[i - 1] + 2
        print res
        return max(res)

s = sys.argv[1]
print Solution().longest(s)
