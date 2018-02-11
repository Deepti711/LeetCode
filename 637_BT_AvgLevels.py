# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        result = []
        
        if not root:
            return res
        
        q = [root]
        while q:
            nodes = []
            total = 0
            count = 0
            while q:
                n = q.pop()
                if n.left:
                    nodes.append(n.left)
                if n.right:
                    nodes.append(n.right)
                
                total += n.val
                count += 1
            
            result.append(total/(float(count)))
            q = nodes
        
        return result