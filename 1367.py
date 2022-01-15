# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        
        if not root: return False

        def match(head, root):
            if not head: return True
            if not root: return False
            if head.val != root.val: return False

            return match(head.next, root.left) or match(head.next, root.right)

        return match(head, root) \
            or self.isSubPath(head, root.left) \
            or self.isSubPath(head, root.right)