# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        from collections import defaultdict
        graph = defaultdict(set)
        # 建图
        def dfs(root):
            if root.left :
                graph[root.val].add(root.left.val)
                graph[root.left.val].add(root.val)
                dfs(root.left)
            if root.right:
                graph[root.val].add(root.right.val)
                graph[root.right.val].add(root.val)
                dfs(root.right)
        dfs(root)
        #print(graph)
        cur = [target.val]
        visited ={target.val}
        while K:
            next_time = []
            while cur:
                tmp = cur.pop()
                for node in graph[tmp]:
                    if node not in visited:
                        visited.add(node)
                        next_time.append(node)
            K -= 1
            cur = next_time
        return cur