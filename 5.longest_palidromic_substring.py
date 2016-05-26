# This is the solution of No.5 problem in LeetCode
# Manacher algorithm
import sys

class Solution(object):
    def longestPalindrome(self, ss):
        s = '#'.join(list(ss))
        s = '#' + s + '#'

        center = right = 0
        p = {}
        p[0] = 0

        for i in range(1, len(s)):
            flag = False
            if i < right:
                j = 2 * center - i

                if p[j] + i < right:
                    p[i] = p[j]
                    flag = True
                else:
                    p[i] = right - i

            else:
                p[i] = 0

            if not flag:
                while (i - 1 - p[i]) >= 0 and (i + 1 + p[i]) < len(s) and s[i - 1 -p[i]] == s[i + 1 +p[i]]:
                    p[i] += 1

            if i + p[i] > right:
                right = i + p[i]
                center = i

            if right == len(s) - 1:
                break

        maxlength = 0
        maxcenter = 0
        for i in range(1, len(s)):
            if p.has_key(i):
                if p[i] > maxlength:
                    maxcenter = i
                    maxlength = p[i]
            else:
                break

        l, r = maxcenter - maxlength, maxcenter + maxlength
        l, r = l / 2, r / 2 - 1

        longest = ss[l : r + 1]

        return longest

myStr = sys.argv[1]

print Solution().longestPalindrome(myStr)
