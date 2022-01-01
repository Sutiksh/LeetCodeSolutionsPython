# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA == None or headB == None:
            return None
        
        aptr = headA
        bptr = headB
        
        while aptr != bptr:
            
            if aptr == None:
                aptr = headB
            else:
                aptr = aptr.next
            
            if bptr == None:
                bptr = headA
            else:
                bptr = bptr.next
            
        
        return aptr