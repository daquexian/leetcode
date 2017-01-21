# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# One pass solution is easy, but this solution is in place.
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        fake_head = ListNode(0)
        fake_head.next = head
        this_node = fake_head
        tail = this_node
        while tail.next is not None:
            tail = tail.next
        new_tail = tail

        next_node = this_node.next
        while next_node is not None:
            while next_node.val >= x:
                new_tail.next = next_node
                this_node.next = next_node.next
                next_node.next = None
                new_tail = next_node
                if next_node == tail:
                    return fake_head.next
                next_node = this_node.next
            if next_node == tail:
                return fake_head.next
            this_node = next_node
            next_node = this_node.next
