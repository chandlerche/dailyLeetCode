class Solution:
    def canPartitionKSubsets(self, nums, k: int) -> bool:
        # 从大到小排序
        nums = sorted(nums, reverse=True)
        sums = sum(nums) // k
        if sums < max(nums) or sum(nums) % k:
            return False
        vis = set()
        # 其中total表示当前集合的总和，times表示已经完成的集合数量
        def DFS(total, times):
            if total == sums:
                times += 1
                total = 0
            if not total and times == k and len(vis) == len(nums):
                return True
            for i in range(len(nums)):
                # 相同的元素，之前没用上现在肯定也用不上
                if i and nums[i] == nums[i-1] and i-1 not in vis:
                    continue
                if i not in vis and total + nums[i] <= sums:
                    vis.add(i)
                    if DFS(total + nums[i], times):
                        return True
                    vis.remove(i)
            return False
        return DFS(0, 0)