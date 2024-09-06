# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        
        """
        1 => 2 => 3 => 4 => 5
        head = 
        temp = head
        prev  = head
        
        """
        # while head:
        #     if head.val in nums:
        #         head = head.next
        #     else:
        ans = []
        nums = set(nums)
        while head:
            if head.val not in nums:
                ans.append(head.val)
            head = head.next
        head = ListNode()
        temp = head
        for i in ans:
            new_node = ListNode(i)
            temp.next = new_node
            temp = new_node
        return head.next

            
            


        