# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return None
        ans = [[root.val]]
        q = deque([root])
        while q:
            lvl = []
            while len(q) > 0:
                node = q.popleft()
                if node.left:
                    lvl.append(node.left)
                if node.right:
                    lvl.append(node.right)
            
            ans.append([l.val for l in lvl]) if lvl else None
            q.extend(lvl)
        
        return ans[::-1]
    
        
        
            