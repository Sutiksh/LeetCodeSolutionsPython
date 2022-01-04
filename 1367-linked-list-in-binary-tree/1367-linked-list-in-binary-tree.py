# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEmptyHead(self, head, root):
         
        # o(k)
        if not head: return True 
        
        if not root: return False
        
        if head.val != root.val: return False
        
        if head:
            head = head.next 
        
        left = self.isEmptyHead(head, root.left)
        right = self.isEmptyHead(head, root.right)
                
        return left or right 
    
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        
        # o(n)
        if root is None or head is None: return False 
        
        if self.isEmptyHead(head, root): return True
        
        left = self.isSubPath(head, root.left)
        right = self.isSubPath(head, root.right)
        
        return left or right