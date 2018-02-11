# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if(head == None):
            return
        if(head.next == None):
            return head
        
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