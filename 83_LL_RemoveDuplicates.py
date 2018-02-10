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
        if(head == None):
            return 
        
        p = head
        if(head.next == None):
            return head
        
        q = head.next
        
        while(q != None):
            if(p.val == q.val):
                q = q.next
                p.next = None
            else:
                p.next = q
                p = q
                q = q.next
            
        return head
        