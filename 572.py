# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        # 判断两棵树是否相同
        def dfs(node1, node2):
            if not node1 and not node2:
                return True
            if node1 and not node2 or node2 and not node1:
                return False
            if node1.val != node2.val:
                return False
            b1 = dfs(node1.left, node2.left)
            b2 = dfs(node1.right, node2.right)
            return True if b1 and b2 else False
        # 层序遍历s，判断每个子树是否和t相同
        queue = deque([s])
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if dfs(node, t):
                    return True
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return False