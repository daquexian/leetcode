# This is the solution of No.6 problem in LeetCode, https://leetcode.com/problems/zigzag-conversion/
# This problem is relatively easy.
import sys
from math import ceil

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        num = numRows * 2 - 2
	if num == 0:
		return s
        ret = ''
        for i in range(numRows):
            for j in range(int(ceil(1.0 * len(s) / num))):
                if num * j + i < len(s):
                    ret += s[num * j + i] 
                    if i != 0 and i != numRows - 1 and num * (j + 1) -i < len(s) :
                        ret += s[num * (j + 1) - i]
                else:
                    break
 
        return ret

s = sys.argv[1]
numRows = eval(sys.argv[2])

print Solution().convert(s, numRows)
