import sys

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_len = len(nums)
        i = farthest = 0
        while i <= farthest:
            farthest = max(farthest, i + nums[i])
            print i, nums[i], farthest
            if farthest >= nums_len - 1:
                return True
            i += 1
        return False

nums = eval(sys.argv[1])
print Solution().canJump(nums)
