# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def symmetric(leftC, rightC):
            if not leftC or not rightC:
                return leftC == rightC
            
            if leftC.val != rightC.val:
                return False
            
            return symmetric(leftC.left, rightC.right) and symmetric(leftC.right, rightC.left)
        
        return symmetric(root.left, root.right)
        
        
        