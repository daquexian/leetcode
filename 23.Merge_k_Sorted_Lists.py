# This is the solution of No.23 problem in LeetCode
# Use heap to reduce the time complexity

import heapq

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        head = None
        for node in lists:
            if node != None:
                heapq.heappush(heap, (node.val, node))
        if len(heap) > 0:
            preNode = head = heapq.heappop(heap)[1]
            if preNode.next != None:
                heapq.heappush(heap, (preNode.next.val, preNode.next))
        while len(heap) > 0:
            node = heapq.heappop(heap)[1]
            preNode.next = node
            preNode = node
            if preNode.next != None:
                heapq.heappush(heap, (node.next.val, node.next))
        return head

