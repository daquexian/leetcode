import sys

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        i = 0
        while i < len(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                nums.remove(nums[i])
                continue
            ret += 1
            i += 1
        return ret

nums = eval(sys.argv[1])
print Solution().removeDuplicates(nums)
print nums
