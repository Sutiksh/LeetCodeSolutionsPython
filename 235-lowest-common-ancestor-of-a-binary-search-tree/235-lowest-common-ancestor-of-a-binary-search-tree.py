# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if p.val < root.val and q.val > root.val:
            return root
        if q.val < root.val and p.val > root.val:
            return root                    
        
        # when p and q are parent and child        
        if root == p or root == q:
            return root
        
        # Travel to left, if both p and q < node
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        # else travel right
        else:
            return self.lowestCommonAncestor(root.right, p, q)    