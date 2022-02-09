# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode], level=0, levels=None) -> List[List[int]]:
        
        if not levels:
            levels = []
            
        if not root:
            return levels
            
        if len(levels) < level + 1:
            levels.append(deque([]))
            
        # Left -> Right
        if level % 2 == 0:
            levels[level].append(root.val)
        # Left <- Right
        else:
            levels[level].appendleft(root.val)
                
                
        self.zigzagLevelOrder(root.left, level + 1, levels)

        self.zigzagLevelOrder(root.right, level + 1, levels)
        
        return levels
                
        