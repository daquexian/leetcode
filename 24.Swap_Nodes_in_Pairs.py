# This is the solution of No.24 problem in LeetCode

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head != None and head.next != None:
            #tmp = head.next
            #head.next = tmp.next
            #tmp.next = head
            #head = tmp
            newHead = head.next
            head.next, newHead.next, head = newHead.next, head, newHead
            
            #preNode = head.next
            #node = preNode.next
            preNode, node = head.next, head.next.next
            if node != None:
                nextNode = node.next
            while node != None and nextNode != None:
                #preNode.next = nextNode
                #node.next = nextNode.next
                #nextNode.next = node
                
                preNode.next, node.next, nextNode.next = nextNode,nextNode.next, node
                
                preNode, node = node, node.next
                #preNode = node
                #node = preNode.next
                if node != None:
                    nextNode = node.next
                    
        return head
