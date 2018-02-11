# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None




class Solution(object):
    
    l = []
    
    def inOrder(self, root):
        
        if(root == None):
            return
    
        self.inOrder(root.left)
        self.l.append(root.val)
        self.inOrder(root.right)
    
    
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.l = []
        self.inOrder(root)
        print(self.l)
        ans = min(abs(self.l[i+1] - self.l[i]) for i in range (len(self.l)-1))
        return ans