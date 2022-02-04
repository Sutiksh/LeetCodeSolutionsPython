# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
                # init
        res = []

        # find
        self.dfs(root, targetSum, res, [])

        # return
        return res

    def dfs(self, root, targetSum, res, stack):
        # corner cases
        if not root:
            return

        # check if leaf value match
        if not root.left and not root.right and root.val == targetSum:
            stack += [root.val]
            res.append(stack)

        # check remains at left subtree
        self.dfs(root.left, targetSum-root.val, res, stack + [root.val])

        # check remains at right subtree
        self.dfs(root.right, targetSum-root.val, res, stack + [root.val])