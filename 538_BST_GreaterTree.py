# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    add = 0
    
    def reverseTraverse(self, root):
        if(root == None):
            return
        self.reverseTraverse(root.right)
        root.val += self.add
        self.add = root.val
        self.reverseTraverse(root.left)
    
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.reverseTraverse(root)
        return root