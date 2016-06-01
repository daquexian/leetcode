# This is the solution of No.11 problem in LeetCode, https://leetcode.com/problems/container-with-most-water/
# Frankly speaking, I can't solve this problem, and I view https://leetcode.com/discuss/14610/very-simple-o-n-solution
# This is absolutely a brilliant solution. I have a lot to learn.

import sys

class Solution(object):
    def maxArea(self, height):
        if len(height) == 0:
            return 0
        i, j = 0, len(height) - 1
        ret = 0
        while(i < j):
#            print min(height[i], height[j]) * (j - i) 
            ret = max(ret, min(height[i], height[j]) * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return ret

height = eval(sys.argv[1])
print Solution().maxArea(height)
