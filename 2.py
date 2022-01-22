# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        sum = 0
        cur = dummy
        p1 , p2 = l1 , l2
        while p1 != None or p2 != None:
            if p1 != None:
                sum += p1.val
                p1 = p1.next
            if p2 != None:
                sum += p2.val
                p2 = p2.next #这里第一次写错，写了p1 = p2.next
            cur.next = ListNode(sum % 10)
            sum = sum // 10
            cur = cur.next
        if  sum == 1:
            cur.next = ListNode(1)
        return dummy.next