'''
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
    Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
    Given m, n satisfy the following condition:
        1 <= m <= n <= length of list.

'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head

        fake_head = ListNode(0)
        fake_head.next = head
        prev_node, this_node, next_node = fake_head, head, head.next
        i = 1
        while i < n:
            if i == m:
                prev1 = prev_node
                this1 = this_node
            elif i > m:
                this_node.next = prev_node

            prev_node, this_node, next_node = this_node, next_node, \
                next_node.next
            i += 1

        this_node.next = prev_node
        prev1.next = this_node
        this1.next = next_node

        return fake_head.next
