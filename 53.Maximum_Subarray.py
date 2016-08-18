# This is the solution of No.53 problem in LeetCode, https://leetcode.com/problems/maximum-subarray/
# It's a classic problem.

import sys

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_list = [] # max_list[i] is max sum of subarrays end with nums[i]
        l = len(nums)
        for i in range(l):
            if i == 0:
                max_list.append(nums[i] if nums[i] > 0 else 0)
            else:
                max_list.append(max_list[i - 1] + nums[i] if max_list[i - 1] + nums[i] > 0 else 0)
        ret = max(max_list)
        if ret == 0:
            return max(nums)
        else:
            return ret

nums = eval(sys.argv[1])
print Solution().maxSubArray(nums)
