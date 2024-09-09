# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dum = ListNode()
        while head:
            new_node = ListNode(head.val)
            head = head.next
            new_node.next = dum.next
            dum.next = new_node
            
        return dum.next