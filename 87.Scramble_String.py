import sys


class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        count = [0] * 26
        if len(s1) != len(s2):
            return False
        if len(s1) == 1:
            return s1 == s2

        for c in s1:
            count[ord(c) - ord('a')] += 1
        for c in s2:
            count[ord(c) - ord('a')] -= 1
        for x in count:
            if x != 0:
                return False

        for i in range(len(s1)):
            if (self.isScramble(s1[:i], s2[:i]) and
                self.isScramble(s1[i:], s2[i:])) \
                    or \
                    (self.isScramble(s1[:i], s2[-i:]) and
                     self.isScramble(s1[i:], s2[:-i])):
                return True
        return False

s1, s2 = sys.argv[1], sys.argv[2]
print(Solution().isScramble(s1, s2))
