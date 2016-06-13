# This is the solution of No.16 problem in LeetCode, https://leetcode.com/problems/3sum-closest/
# This is similar with No.15

import sys

class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        minDiff = 1 << 31 - 1
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
                diff = abs(mySum - target)
                if diff < minDiff:
                    minDiff = diff
                    ret = mySum
                if mySum < target:
                    j += 1
                elif mySum > target:
                    k -= 1
                else:
                    return target
        return ret

nums = eval(sys.argv[1])
target = eval(sys.argv[2])
print Solution().threeSumClosest(nums, target)
