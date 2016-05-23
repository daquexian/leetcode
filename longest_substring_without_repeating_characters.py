# perfect O(n) solution
import sys

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        start = maxLength = 0
        usedChars = {}
        for i in range(len(s)):
            if s[i] in usedChars and start <= usedChars[s[i]]:
                start = usedChars[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)
            usedChars[s[i]] = i
        return maxLength
s = sys.argv[1]
print Solution().lengthOfLongestSubstring(s)
