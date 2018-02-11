# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        if(head == None):
            return
        
        p = head
        
        while(p.val == val):
            if(p.next != None):
                p = p.next
            else:
                if(p.val == val):
                    return
                
        head = p
        
        if(head.next == None):
            if(head.val == val):
                return None
            else:
                return head
        
        q = p.next
        
        while(q != None):
            if(q.val == val):
                p.next = q.next
                q = q.next
            else:
                p = p.next
                q = q.next
        
        return head