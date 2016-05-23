import sys
class ListNode(object): 
    def __init__(self, x):
       self.val = x 
       self.next = None
class Solution(object):
    def addTwoNumbers(self, L1, L2):
        flag = 0
        headNode, preNode = None, None
        while L1 != None and L2 != None:
            val = L1.val + L2.val + flag
            flag = val / 10
            val %= 10
            newNode = ListNode(val)
            if headNode == None:
                headNode = newNode
            if preNode != None:
                preNode.next = newNode
            preNode = newNode
            L1, L2 = L1.next, L2.next
        L = L1 if L1 != None else L2
        while L != None or flag != 0:
            if L == None:
                newNode = ListNode(flag)
                preNode.next = newNode
                flag = 0
            else:
                val = L.val + flag
                flag = val / 10
                val %= 10
                newNode = ListNode(val)
                if headNode == None:
                    headNode = newNode
                if preNode != None:
                    preNode.next = newNode
                preNode = newNode
                L = L.next
        return headNode

def list2LinkedList(lst):
    headNode,preNode = None, None
    for i in lst:
        newNode = ListNode(i)
        if headNode == None:
            headNode = newNode
        if preNode != None:
            preNode.next = newNode
        preNode = newNode
    return headNode

def printLL(node):
    while node != None:
        print node.val
        node = node.next
arg1 = eval(sys.argv[1])
arg2 = eval(sys.argv[2])

L1 = list2LinkedList(arg1)
L2 = list2LinkedList(arg2)

printLL(Solution().addTwoNumbers(L1, L2))
