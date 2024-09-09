# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        rev = None
        current = slow
        while current:
            next_node = current.next
            current.next = rev
            rev = current
            current = next_node
        left, right = head, rev
        while right:
            if right.val !=left.val:
                return False
            left = left.next
            right = right.next
        return True
