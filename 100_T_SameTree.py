# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
        
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        def checkEqual(p, q):
            if (not p and not q):
                return True
            if(not p or not q):
                return False
            
            if(p.val == q.val):
                return checkEqual(p.left, q.left) and checkEqual(p.right, q.right)
            
            return False
        return checkEqual(p,q)
        
    