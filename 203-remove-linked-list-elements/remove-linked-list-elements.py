# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy  = ListNode()
        start = dummy
        while head:
            if head.val == val:
                head = head.next
            else:
                dummy.next = head
                dummy = dummy.next
                head = head.next
        dummy.next = head
        
        return start.next

