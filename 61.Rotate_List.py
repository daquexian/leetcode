import sys

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return head
        length = 1
        tail = head
        while tail.next != None:
            tail = tail.next
            length += 1
        p = head
        k %= length
        for i in range(length - k - 1):
            p = p.next
        tail.next = head
        head = p.next
        p.next = None
        '''
        p1, p2 = head, head
        k %= length
        for i in range(k):
            p1 = p1.next
        while p1.next != None:
            p1, p2 = p1.next, p2.next
        p1.next = head
        head = p2.next
        p2.next = None
        '''
        return head
