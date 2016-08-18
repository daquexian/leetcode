import sys

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        nums.sort()
        while True:
            #print nums
            ret.append(nums[:])
            nums = self.next_permutation(nums)
            if nums == None:
                break
        return ret

    def next_permutation(self, p):
        l = len(p)
        for i in reversed(range(l - 1)):
            if p[i] < p[i + 1]:
                for j in reversed(range(i + 1, l)):
                    if p[j] > p[i]:
                        p[i], p[j] = p[j], p[i]
                        break
                p = p[:i + 1] + list(reversed(p[i + 1:]))
                return p
        return None

nums = eval(sys.argv[1])
print Solution().permute(nums)
