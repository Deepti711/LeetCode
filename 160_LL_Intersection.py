# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def listLength(node):
    l = 0
    while(node.next!= None):
        node = node.next
        l += 1
            
    return l

def traverse(node, length):
    while(length != 0):
        node = node.next
        length -= 1
        
    return node
    
class Solution(object):

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        if(headA == None or headB == None):
            return None
        
        
        lA = listLength(headA)
        lB = listLength(headB)
        
        p = headA
        q = headB
        
        if(lA > lB):
            p = traverse(headA, lA-lB)
        if(lB > lA):
            q = traverse(headB, lB-lA)
        
        while(p != None and q != None):
            if(p.val == q.val):
                return p
            p = p.next
            q = q.next
        
        return None