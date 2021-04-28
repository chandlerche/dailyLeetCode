class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:

        self.res = 0
        def isValid(root, t1, t2):
            if not root:
                return 0
            if root.val >= t2 or root.val <= t1:
                return float("-inf")
            return 1 + isValid(root.left, t1, root.val) + isValid(root.right, root.val, t2)

        def helper(root):
            if not root:
                return 
            self.res = max(self.res, isValid(root,float("-inf"), float("inf")) )
            helper(root.left)
            helper(root.right)
        helper(root)
        return self.res