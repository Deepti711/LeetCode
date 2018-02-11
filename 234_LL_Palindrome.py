# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def reverseList(head):
    currentNode = head
    previousNode = None
    nextNode = None
        
    while(currentNode != None):
        nextNode = currentNode.next
        currentNode.next = previousNode
        previousNode = currentNode
        currentNode = nextNode
        
    head = previousNode
    return head

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if(head == None):
            return True
        
        fast = head
        slow = head
        while(fast.next != None and fast.next.next != None):
            fast = fast.next.next
            slow = slow.next
        
        l2 = reverseList(slow)
        l1 = head
        
        while(l1 != None and l2 != None):
            if(l1.val != l2.val):
                return False
            
            l1 = l1.next
            l2 = l2.next
        
        return True
        