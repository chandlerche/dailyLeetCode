class Solution:

    def inorderSuccessor(self , root , p):
        res = None
        while root is not None:
            if root.val <= p:
                root = root.right
            else:
                res = root
                root = root.left
        return res.val if res is not None else None