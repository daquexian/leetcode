import sys
import collections

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need = collections.Counter(t)
        missing = len(t)
        bottom = 0
        minBottom, minTop = 0, len(s)
        
        for i, a in enumerate(s):
            if need[a] > 0:
                missing -= 1
            need[a] -= 1
            while True:
                if bottom < len(s) and need[s[bottom]] < 0:
                    need[s[bottom]] += 1
                    bottom += 1
                else:
                    break
            if missing == 0 and (minTop - minBottom) > (i - bottom):
                minTop, minBottom = i, bottom

        if minTop == len(s):
            return ""
        return s[minBottom: minTop + 1]
        
s = sys.argv[1]
t = sys.argv[2]

print(Solution().minWindow(s, t))

