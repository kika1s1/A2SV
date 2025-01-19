# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr = []
        temp = head
        while temp:
            arr.append(temp.val)
            temp = temp.next
        upto = (len(arr)//k)*k
        for i in range(0, upto, k):
            arr = arr[:i] + arr[i:i+k][::-1] + arr[i+k:]
        i = 0
        temp = head
        while temp:
            temp.val = arr[i]
            i +=1
            temp = temp.next
        return head