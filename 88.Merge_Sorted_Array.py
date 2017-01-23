class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = j = 0

        while i < m and j < n:
            if nums1[i] > nums2[j]:
                nums1.insert(i, nums2[j])
                nums1.pop()
                m, j = m + 1, j + 1
            i += 1

        while j < n:
            nums1[i] = nums2[j]
            i, j = i + 1, j + 1

nums1 = [1, 1, 1, 2, 3, 5, 7, 0, 0, 0, 0, 0, 0]
nums2 = [2, 3, 4, 6, 8, 9]
Solution().merge(nums1, 7, nums2, len(nums2))
print(nums1)
