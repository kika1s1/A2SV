# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nums = []
        for num in lists:
            while num:
                nums.append(num.val)
                num = num.next
        nums.sort()
        head = ListNode()
        temp = head
        for num in nums:
            new_node = ListNode(num)
            temp.next =  new_node 
            temp = new_node
        return head.next