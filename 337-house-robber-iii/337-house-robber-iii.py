# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            # if no child node
            if not node.left and not node.right:
                return [0,node.val]
            # return 0,0 incase if child is not present for a node
            childl = helper(node.left) if node.left else [0,0]
            childr = helper(node.right) if node.right else [0,0]
            #nc - not choosing current node means we could have either choosen child or not. 
            #hence we take max from each child and add it.
            nc = max(childl)+max(childr)
            #c - choosing current node means, strictly its child node not choosen.
            # hence take nc value from each of its child node and add it to node.val
            c = childl[0]+childr[0]+node.val
            return [nc,c]
        return max(helper(root))