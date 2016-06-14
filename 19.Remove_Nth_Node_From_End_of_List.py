# This is the solution of No.19 problem in LeetCode, https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Use two pointers

class Solution(object):
    def removeNthFromEnd(self, head, n):
        pter1 = pter2 = head
        for i in range(n + 1):
            if pter1 == None:
                return head.next
            pter1 = pter1.next
        while pter1 != None:
            pter1 = pter1.next
            pter2 = pter2.next
        pter2.next = pter2.next.next
        return head
