# This is the solution of No.81 problem in LeetCode
# Similar with that of No.33, only deal with the condition of l[mid]  = l[left]

import sys

class Solution:
    def search(self, l, a):
        left, right, mid = 0, len(l) - 1, (len(l) - 1) / 2
        while left <= right:
            # At first, compare and return if the both equal, or it will go wrong, e.g. l = [3, 1], a = 1
            for i in [left, right, mid]:
                if a == l[i]:
                    return True
            if l[mid] > l[left]:  #no less than a half elements in array are rotated
                if l[left] < a < l[mid]:
                    left, right, mid = left, mid - 1, (left + mid - 1) / 2
                elif a > l[mid] or a < l[left]:
                    left, right, mid = mid + 1, right, (mid + 1 + right) / 2
#                elif a == l[left]:
#                    return left
#                else:
#                    return mid
            elif l[mid] < l[left]:
                if l[mid] < a < l[right]:
                    left, right, mid = mid + 1, right, (mid + 1 + right) / 2
                elif a > l[right] or a < l[mid]:
                    left, right, mid = left, mid - 1, (left + mid - 1) / 2
#                elif a == l[right]:
#                    return right
#                else:
#                    return mid
            else:
                left, right, mid = left + 1, right, (left + 1 + right) / 2
        return False

l = eval(sys.argv[1])
a = eval(sys.argv[2])

print Solution().search(l, a)
