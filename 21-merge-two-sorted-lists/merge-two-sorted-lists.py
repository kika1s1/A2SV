# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        tail = ListNode()
        new_list = tail
        while list1 and list2:
            if list1.val < list2.val:
                new_node = ListNode(list1.val)
                tail.next = new_node
                tail  = new_node
                list1 = list1.next
            else:
                new_node = ListNode(list2.val)
                tail.next = new_node
                tail  = new_node
                list2 = list2.next
        while list1:
            new_node = ListNode(list1.val)
            tail.next = new_node
            tail  = new_node
            list1 = list1.next
        while list2:

            new_node = ListNode(list2.val)
            tail.next = new_node
            tail  = new_node
            list2 = list2.next
        return new_list.next




