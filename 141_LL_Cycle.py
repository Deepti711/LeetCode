# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        p = head
        if(head == None):
            return False
        if(head.next == None):
            return False
        if(head.next.next != None):
            q = head.next.next
        else:
            return False
        
        while(q.next != None and q.next.next != None):
            if(p == q):
                return True
            p = p.next
            q = q.next.next
            
         
        return False