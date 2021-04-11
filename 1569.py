class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        def dfs(nums):
            if not nums: return 1
            l, r = [], []
            root = nums[0]
            for n in nums[1:]:
                if n < root: l.append(n)
                if n > root: r.append(n)
            a, b = len(l), len(r)        
            m, n = dfs(l), dfs(r)        
            return m*n*comb(a + b, a)%(10**9 + 7)
        return dfs(nums) - 1