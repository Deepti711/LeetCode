# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if(l1 == None and l2 == None):
            return
        
        if(l1 == None and l2 != None):
            return l2
        
        if(l2 == None and l1 != None):
            return l1
        
        if(l1.val <= l2.val):
            newNode = ListNode(l1.val)
            l1 = l1.next
        else:
            newNode = ListNode(l2.val)
            l2 = l2.next
                
        head = previous = newNode
        
        while(l1 != None and l2 != None):
            if(l1.val <= l2.val):
                newNode = ListNode(l1.val)
                l1 = l1.next
            else:
                newNode = ListNode(l2.val)
                l2 = l2.next
        
            previous.next = newNode
            previous = newNode
          
        previous.next = l1 or l2
            
        return head