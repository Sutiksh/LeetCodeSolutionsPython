# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head
        
        left, right = ListNode(), ListNode()
        ltail, rtail = left, right
        tmp = head
        while tmp:
            if tmp.val < x:
                ltail.next = tmp
                ltail = ltail.next
            else:
                rtail.next = tmp
                rtail = rtail.next
            tmp = tmp.next
        
        ltail.next = right.next
        rtail.next = None
        return left.next
            
        
        
        
        
        