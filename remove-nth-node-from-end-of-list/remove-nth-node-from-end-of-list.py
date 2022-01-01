# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = slow = head 
        for i in range(n):
            fast = fast.next 

        if fast is None: 
            return head.next 

        while fast.next:
            fast = fast.next  #After this we are increasing both fast and head by 1 step each
            slow = slow.next


        slow.next = slow.next.next 
        return head
        
        
        