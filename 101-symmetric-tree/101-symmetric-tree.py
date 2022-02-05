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
        
        return self.areSymmetric(root.left, root.right)
    
    def areSymmetric(self, leftC, rightC):
        if leftC == None or rightC == None:
            return leftC == rightC
        
        if leftC.val != rightC.val:
            return False
        
        return self.areSymmetric(leftC.left, rightC.right) and self.areSymmetric(leftC.right, rightC.left)
        
        
        
        