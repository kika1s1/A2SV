# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse_segment(start, end):
            prev, curr = None, start
            while curr != end:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev  
        
        
        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy
        
        while True:
            group_start = prev_group_end.next
            group_end = prev_group_end
            for _ in range(k):
                group_end = group_end.next
                if not group_end:
                    return dummy.next  
            
            
            next_group_start = group_end.next
            new_group_head = reverse_segment(group_start, group_end.next)
            
            
            prev_group_end.next = new_group_head
            group_start.next = next_group_start
            
            
            prev_group_end = group_start
