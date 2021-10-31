class Solution:

    # dfs 贪心，肯定是k个板子全插入最好
    def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
        n = len(nums)
        tot = sum(nums)

        from functools import lru_cache
        @lru_cache(None)
        def dfs(cur, pre): # 表示的是 nums[pre:] 中 还可以插入 k 块板子的时候，最小差
            if cur == 0:
                h = max(nums[pre:], default=0)
                return h*(n - pre)

            ans = float('inf')
            h = nums[pre]
            for j in range(pre+1, min(n - cur + 2, n)): # 遍历下一块板子的起始位置
                ans = min(dfs(cur-1, j) + (j - pre)*h, ans)
                h = max(h, nums[j])
            return ans

        return dfs(k, 0) - tot