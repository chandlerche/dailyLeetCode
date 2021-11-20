class Solution:
    def numberOfWays(self, n):
        res = 1
        for i in xrange(1, n / 2 + 1):
            res *= n - i + 1
            res /= i
        return res / (n / 2 + 1) % (10**9 + 7)