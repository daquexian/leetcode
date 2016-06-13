# This is the solution of No.15 problem in LeetCode, https://leetcode.com/problems/3sum/

import sys

class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        ret = []
        for i in range(len(nums)):
            if i - 1 >= 0 and nums[i - 1] == nums[i]:
                continue
            j, k = i + 1, len(nums) - 1
            while j < k:
                if j - 1 >= i + 1 and nums[j - 1] == nums[j]:
                    j += 1
                    continue
                if k + 1 < len(nums) and nums[k + 1] == nums[k]:
                    k -= 1
                    continue
                mySum = nums[i] + nums[j] + nums[k]
                if mySum < 0:
                    j += 1
                elif mySum > 0:
                    k -= 1
                else:
                    ret.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
        return ret

nums = eval(sys.argv[1])
print Solution().threeSum(nums)
