# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from queue import Queue

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return ''
        res = []
        queue = Queue()
        queue.put(root)
        while queue.empty() == False:
            cur = queue.get()
            if cur is None:
                res.append('null ')
                continue
            res.append('%d '%cur.val)
            queue.put(cur.left)
            queue.put(cur.right)
        return ''.join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '': return None
        strs = data.split(' ')
        root = TreeNode(int(strs[0]))
        queue = Queue()
        queue.put(root)

        i = 1
        while i < len(strs) - 1:
            cur = queue.get() # 先把queue中元素弹出
            if strs[i] != 'null':
                cur.left = TreeNode(int(strs[i])) # 把该值变成左结点
                queue.put(cur.left) # 压入队列的作用是为了帮他们依次找自己孩子结点
            i += 1
            if strs[i] != 'null':
                cur.right = TreeNode(int(strs[i])) # 把该值变成右结点
                queue.put(cur.right)
            i += 1
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))