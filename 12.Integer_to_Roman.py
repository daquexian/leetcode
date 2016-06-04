# This is the solution of No.12 problem in LeetCode, https://leetcode.com/problems/integer-to-roman/
# This problem is relatively easy, However, the knowledge of the rule of roman numeral is needed.

import sys

class Solution:
    def intToRoman2(self, startingDigit, digitnum):
        list_1 = ['I', 'X', 'C', 'M']
        list_5 = ['V', 'L', 'D', '*']
        if startingDigit <= 3:
            return list_1[digitnum - 1] * startingDigit
        elif startingDigit == 4:
            return list_1[digitnum - 1] + list_5[digitnum - 1]
        elif startingDigit == 5:
            return list_5[digitnum - 1]
        elif startingDigit <= 8:
            return list_5[digitnum - 1] + list_1[digitnum - 1] * (startingDigit - 5)
        elif startingDigit == 9:
            return list_1[digitnum - 1] + list_1[digitnum]

    def intToRoman(self, num):
        ret = ''
        for i in range(len(str(num))):
            ret += self.intToRoman2(int(str(num)[i]), len(str(num)) - i)
        return ret

num = eval(sys.argv[1])
print Solution().intToRoman(num)
