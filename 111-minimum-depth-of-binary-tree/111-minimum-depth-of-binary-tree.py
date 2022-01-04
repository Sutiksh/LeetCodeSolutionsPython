# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return self.dfs(root)
    def dfs(self, node, res=9999, lvl=1):
        if not node.left and not node.right and lvl < res:
            return lvl
        if node.left:
            res = self.dfs(node.left, res, lvl+1)
        if node.right:
            res = self.dfs(node.right, res, lvl+1)
        return res
        