# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummyNode = ListNode()
        head = dummyNode
        while l1 and l2:
            add = l1.val + l2.val + carry
            if add < 10:
                temp  = ListNode(add)
                head.next = temp
                head = temp
                carry = 0
            else:
                q = add%10
                carry = add // 10
                temp = ListNode(q)
                head.next = temp
                head = temp
            l1, l2 = l1.next, l2.next
        while l1:
            add = l1.val + carry
            if add > 10:
                temp  = ListNode(add)
                head.next = temp
                head = temp
                carry = 0
            else:
                q = add%10
                carry = add // 10
                temp = ListNode(q)
                head.next = temp
                head = temp
            l1 = l1.next
        while l2:
            add = l2.val + carry
            if add > 10:
                temp  = ListNode(add)
                head.next = temp
                head = temp
                carry = 0
            else:
                q = add%10
                carry = add // 10
                temp = ListNode(q)
                head.next = temp
                head = temp
            l2 = l2.next
        if carry:
                temp = ListNode(carry)
                head.next = temp
                head = temp

        return dummyNode.next


