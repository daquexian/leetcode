import sys

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = j = 0
        nums_len = len(nums)
        while j < nums_len:
            while j < nums_len and nums[j] == val:
                j += 1
            if j < nums_len:
                nums[i] = nums[j]
                i += 1
                j += 1
        
        print nums
        return nums_len - (j - i)

nums = eval(sys.argv[1])
val = eval(sys.argv[2])

print Solution().removeElement(nums, val)
