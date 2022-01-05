# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None:
            return None
        # if node is p or q then return that node to the node
        if root.val == p.val or root.val == q.val:
            return root
        # finding left and right sub tree
        left_part = self.lowestCommonAncestor(root.left, p, q)
        right_part = self.lowestCommonAncestor(root.right, p, q)

        # if both left and right subtree are none then return node to the parent 
        if left_part != None and right_part != None:
            return root
        # if one sub tree is null and one sub tree is not null
        else:
            return left_part if left_part else right_part
        return root 