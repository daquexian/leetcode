import sys

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        t = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i + 1] > nums[i]:
                t = i
                break
        else:
            nums.reverse()
            return
        n = t + 1
        for i in range(len(nums) - 1, t, -1):
            if nums[i] > nums[t]:
                n = i
                break
        nums[t], nums[n] = nums[n], nums[t]
        #tmp = nums[t + 1:]
        #tmp.reverse()
        #nums[t + 1:] = tmp
        nums[t + 1:] = nums[:t:-1]

nums = eval(sys.argv[1])
Solution().nextPermutation(nums)
print nums
