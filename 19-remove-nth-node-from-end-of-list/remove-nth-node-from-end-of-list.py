# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        current = head
        prev = head
        counter = 1

        while current.next:
            if counter > n:
                prev = prev.next
            current = current.next
            counter += 1
        
        if counter == n:
            return head.next
        
        if current == head:
            # we know that the length of the list is 1
            if n == 1:
                return None
        else:
            prev.next = prev.next.next
        
        
        return head
        