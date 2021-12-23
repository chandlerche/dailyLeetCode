# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        max_width = 0
        queue = collections.deque([(root, 1)])
        while queue:
            max_width = max(max_width, queue[-1][1] - queue[0][1] + 1)
            for _ in range(len(queue)):
                node, idx = queue.popleft()

                if node.left:  queue.append((node.left,  idx * 2))
                if node.right: queue.append((node.right, idx * 2 + 1))

        return max_width