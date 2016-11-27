import sys

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for n in nums:
            if i < 1 or n > nums[i - 1]:
                nums[i] = n
                i += 1
        print nums[:i]
        return i

nums = eval(sys.argv[1])
print Solution().removeDuplicates(nums)
