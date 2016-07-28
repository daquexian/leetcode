# This is the solution of No.34 problem in LeetCode, https://leetcode.com/problems/search-for-a-range/
# It's a variant of binary search
import sys

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lower_bound = upper_bound = -1
        left, right, mid = 0, len(nums) - 1, (len(nums) - 1) / 2
        while left <= right:
            if target < nums[mid]:
                left, right, mid = left, mid - 1, (left + mid - 1) / 2
            elif target > nums[mid]:
                left, right, mid = mid + 1, right, (mid + 1 + right) / 2
            elif mid > 0 and nums[mid] == nums[mid - 1]:
                left, right, mid = left, mid - 1, (left + mid - 1) / 2
            else:
                lower_bound = mid
                break
        left, right, mid = 0, len(nums) - 1, (len(nums) - 1) / 2
        while left <= right:
            print mid
            if target < nums[mid]:
                left, right, mid = left, mid - 1, (left + mid - 1) / 2
            elif target > nums[mid]:
                left, right, mid = mid + 1, right, (mid + 1 + right) / 2
            elif mid < len(nums) - 1 and nums[mid] == nums[mid + 1]:
                left, right, mid = mid + 1, right, (mid + 1 + right) / 2
            else:
                upper_bound = mid
                break
        return [lower_bound, upper_bound]
                
nums = eval(sys.argv[1])
target = eval(sys.argv[2])

print Solution().searchRange(nums, target)
