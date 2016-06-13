# This is the solution of No.18 problem in LeetCode, https://leetcode.com/problems/4sum/
# This is similar with 3Sum. Time will be out without line 13, 14

import sys

class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        ret = []
        for i in range(len(nums)):
            if i - 1 >= 0 and nums[i - 1] == nums[i]:
                continue
            for l in range(i + 1, len(nums)):
                if l + 2 < len(nums) and nums[i] + nums[l] + nums[l + 1] + nums[l + 2] > target:
                    break
                if l - 1 >= i + 1 and nums[l - 1] == nums[l]:
                    continue
                j, k = l + 1, len(nums) - 1
                while j < k:
                    if j - 1 >= l + 1 and nums[j - 1] == nums[j]:
                        j += 1
                        continue
                    if k + 1 < len(nums) and nums[k + 1] == nums[k]:
                        k -= 1
                        continue
                    mySum = nums[i] + nums[j] + nums[k] + nums[l]
                    if mySum < target:
                        j += 1
                    elif mySum > target:
                        k -= 1
                    else:
                        ret.append([nums[i], nums[l], nums[j], nums[k]])
                        j += 1
                        k -= 1
        return ret

nums = eval(sys.argv[1])
target = eval(sys.argv[2])
print Solution().fourSum(nums, target)
