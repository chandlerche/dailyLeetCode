class Solution:

res = 0

def longestConsecutive(self , root):
    if root is None: return 0
    self.helper(root , 0 , root.val)
    return self.res

def helper(self , root , maxval , target):
    if root is None: return
    if root.val == target:
        maxval += 1
    else:
        maxval = 1
    self.res = max(maxval , self.res)
    self.helper(root.left , maxval , root.val + 1)
    self.helper(root.right , maxval , root.val + 1)