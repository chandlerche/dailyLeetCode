# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
	count = 0
	def pathSum(self, root, targetSum):
		if not root:
			return 0
		self.getsum([], root, targetSum)
		return self.count

	def getsum(self, s_list, root, targetSum):
		if not root:
			return
		val = root.val
		s_list = [s+root.val for s in s_list]
		s_list.append(val)
		if targetSum in s_list:
			self.count += s_list.count(targetSum)
		if root.left != None:
			self.getsum(s_list, root.left, targetSum)
		if root.right != None:
			self.getsum(s_list, root.right, targetSum)