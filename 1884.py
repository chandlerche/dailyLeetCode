class Solution(object):
    def twoEggDrop(self, n):
        cur = 0
        res = 0
        while cur < n:
            res += 1
            cur += res
        return res