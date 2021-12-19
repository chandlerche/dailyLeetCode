class Solution:

    def closestKValues(self , res , root , target , k):
        res = []
        self.helper(res , root , target , k)
        return res

    def helper(self, res , root , target , k):
        if root is None: return
        self.helper(res , root.left , target , k)
        if len(res) == k:
            if abs(target - root.val) < abs(target - res[0]):
                del res[0]
            else:
                return
        res.append(root.val)
        self.helper(res , root.right , target , k)