import heapq

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        dic = {}
        for x in lists:
            if x != None:
                heapq.heappush(heap, x.val)
                dic[x.val] = x
        if len(heap) == 0:
            return []
        
        head = dic[heapq.heappop(heap)]
        if head.next != None:
            heapq.heappush(heap, head.next.val)
            dic[head.next.val] = head.next
        node = head
        while(len(heap) > 0):
            i = heapq.heappop(heap)
            x = dic[i]
            node.next = x
            if x.next != None:
                heapq.heappush(heap, x.next.val)
                dic[x.next.val] = x.next
            node = x
        return head
