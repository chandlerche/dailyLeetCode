# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.cur = root


    def next(self) -> int:
        while self.cur is not None:
            self.stack.append(self.cur)
            self.cur = self.cur.left
        node = self.stack.pop()
        self.cur = node.right
        return node.val


    def hasNext(self) -> bool:
        # 用两个条件验证，因为一开始stack为空，cur不为空
        return len(self.stack) > 0 or self.cur is not None



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()