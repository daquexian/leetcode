# This is the solution of No.35 problem in LeetCode,
# https://leetcode.com/problems/search-insert-position/
# It's a variant of binary search.

import sys


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        left, right, mid = 0, len(nums) - 1, (len(nums) - 1) / 2
        while left <= right:
            for i in (left, right, mid):
                if nums[i] == target:
                    return i
            if nums[left] > target:
                return left
            if nums[right] < target:
                return right + 1
            if nums[mid] < target:
                left, right, mid = mid + 1, right, (mid + 1 + right) / 2
            else:
                left, right, mid = left, mid - 1, (left + mid - 1) / 2

nums = eval(sys.argv[1])
target = eval(sys.argv[2])
print(Solution().searchInsert(nums, target))
