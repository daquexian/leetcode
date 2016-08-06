# This is No.42 problem in LeetCode, https://leetcode.com/problems/trapping-rain-water/
# Traversal two times. For the first time calculate water from beginning to the rightest wall among walls with max height, and save the index of this wall. Travelsal from rightest to the wall for the second time, and calculate the water.

import sys

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_height1 = max_height2 = 0
        ret = candidate = 0
        for i in range(len(height)):
            if height[i] < max_height1:
                candidate += max_height1 - height[i]
            else:
                ret += candidate
                candidate = 0
                max_height1 = height[i]
        candidate = 0
        for i in range(len(height) - 1, -1, -1):
            if height[i] == max_height1:
                ret += candidate
                break
            if height[i] < max_height2:
                candidate += max_height2 - height[i]
            else:
                ret += candidate
                candidate = 0
                max_height2 = height[i]
        return ret
            
height = eval(sys.argv[1])
print Solution().trap(height)
