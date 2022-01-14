# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.ST = dict()
        maxSum = 0
        self.checkBST(root)
        for key in self.ST.keys():
            if self.ST[key] > maxSum:
                maxSum = self.ST[key]
        return maxSum

    def checkBST(self, root):
        if root is  None:
            return True, 2147483647, -2147483648, 0
        l_flag, l_min, l_max, l_sum = self.checkBST(root.left)
        r_flag, r_min, r_max, r_sum = self.checkBST(root.right)
        nsum = l_sum + r_sum + root.val
        if l_flag and r_flag and root.val > l_max and root.val < r_min:
            self.ST[root] = nsum
            rel = (True, min(root.val, l_min), max(root.val, r_max), nsum)
        else:
            rel = (False, min(l_min, r_min, root.val), max(l_max, r_max, root.val), nsum)
        return rel