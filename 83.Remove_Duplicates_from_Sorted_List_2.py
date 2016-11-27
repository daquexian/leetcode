# similar with No.82, only delete one line

import sys

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # Not good
        '''
        while head != None and head.next != None and head.next.val == head.val:
            while head.next != None and head.next.val == head.val:
                head = head.next
            head = head.next
        '''
        
        # Fake head, great
        fake_head = ListNode(-1)
        fake_head.next = head

        node = fake_head
        while node != None and node.next != None:
            while node.next != None and node.next.next != None and node.next.val == node.next.next.val:
                while node.next != None and node.next.next != None and node.next.val == node.next.next.val:
                    self.deleteNextNode(node)
            node = node.next
        return fake_head.next
    def deleteNextNode(self, node):
        node.next = node.next.next
