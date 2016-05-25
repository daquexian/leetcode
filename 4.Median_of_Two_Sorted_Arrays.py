'''
This is solution of No.4 problem in Leetcode, https://leetcode.com/problems/median-of-two-sorted-arrays/

The explanation is in https://leetcode.com/discuss/15790/share-my-o-log-min-m-n-solution-with-explanation

Line 8 and 13 to 16 is my first-version code. They are obviously not efficient
'''

import sys

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        n1, n2 = len(nums1), len(nums2)
        #left, right = 0, n1    
        left, right = max(0, (n1 - n2) / 2), min(n1, (n1 + n2) / 2)
        i = (left + right) / 2
        while(True):
            j = (n1 + n2) / 2 - i
            #if j > n2:
            #    i = (n1 - n2) / 2
            #elif j < 0:
            #    i = (n1 + n2) / 2
            if i > 0 and j < n2 and nums1[i - 1] > nums2[j]:
                right = i - 1
                i = (left + right) / 2
            elif j > 0 and i < n1 and nums1[i] < nums2[j - 1]:
                left = i + 1
                i = (left + right) / 2
            else:
                if (n1 + n2) & 1 == 0:
                    return (self.myMin(i, j, n1, n2, nums1, nums2) + self.myMax(i - 1, j - 1, n1, n2, nums1, nums2))/2.0
                else:
                    return self.myMin(i, j, n1, n2, nums1, nums2)

    # use myMax and myMin to handle edge values
    def myMax(self, i, j, n1, n2, nums1, nums2):
        if 0 <= i < n1 and 0 <= j < n2:
            return max(nums1[i], nums2[j])
        elif i < 0 or i >= n1:
            return nums2[j]
        elif j < 0 or j >= n2:
            return nums1[i]
    def myMin(self, i, j, n1, n2, nums1, nums2):
        if 0 <= i < n1 and 0 <= j < n2:
            return min(nums1[i], nums2[j])
        elif i < 0 or i >= n1:
            return nums2[j]
        elif j < 0 or j >= n2:
            return nums1[i]

nums1 = eval(sys.argv[1])
nums2 = eval(sys.argv[2])

print Solution().findMedianSortedArrays(nums1, nums2)
