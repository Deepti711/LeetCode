# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None



class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        if(head == None):
            return
        
        if(head.next == None or k == 0):
            return head
        
        
        l = 1
        node = head
        while(node.next!= None):
            node = node.next
            l += 1
        
        node.next = head
        k = k % l
    
        p = head
        for i in range(l-k, 1, -1):
            print(i)
            p = p.next
        
        head = p.next
        p.next = None
        
        '''
        while (k > 0):
            
            p = q = head
            while(p.next != None):
                q = p
                p = p.next
                
            newHead = p
            q.next = None
            newHead.next = head
            head = newHead
            k -= 1
        '''
        return head