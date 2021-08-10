# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while head:
            if head.val == val:
                head = head.next
            else:
                head.next = self.removeElements(head.next, val)
                return head