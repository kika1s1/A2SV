# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lst = []
        temp = head
        while temp:
            lst.append(temp.val)
            temp = temp.next
        cnt = 0
        temp = head
        while temp:
            if temp.val !=lst[-1-cnt]:
                return False
            cnt +=1
            temp = temp.next
        return True
        