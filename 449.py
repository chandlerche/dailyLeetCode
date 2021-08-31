# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        def preorder(root):
            out = []
            if root:
                out += [str(root.val)]
                out += preorder(root.left)
                out += preorder(root.right)
            return out
        return ','.join(preorder(root))
        
    def deserialize(self, data):
        if not data:
            return None
        def buildTree(pre_o, in_o):
            if not pre_o:
                return None
            mid = pre_o[0]
            i = in_o.index(mid)
            root = TreeNode(mid)
            root.left = buildTree(pre_o[1:i + 1], in_o[:i])
            root.right = buildTree(pre_o[i + 1:], in_o[i + 1:])
            return root
        pre_o = list(map(int, data.split(',')))
        in_o = sorted(pre_o)
        return buildTree(pre_o, in_o)

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans