# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def longestUnivaluePath(self,root):
		ans=0
		def dfs(root):
			nonlocal ans
			if root:
				le=dfs(root.left)+1
				if not root.left or root.left.val!=root.val:
					le=0
				ri=dfs(root.right)+1
				if not root.right or root.right.val!=root.val:
					ri=0
				ans=max(ans,le+ri)
				return max(le,ri)
			return 0
		return (dfs(root) and False) or ans