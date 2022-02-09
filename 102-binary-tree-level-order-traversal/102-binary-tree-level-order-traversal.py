# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        q = collections.deque()
        q.append(root)
        while q:
            n = len(q)
            lvl = []
            for _ in range(n):
                node = q.popleft()
                if node:
                    lvl.append(node.val)
                    for child in [node.left, node.right]:
                        if child is not None:
                            q.append(child)
            if lvl:
                ans.append(lvl)
        return ans
