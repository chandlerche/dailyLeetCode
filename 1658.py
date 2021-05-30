class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # 将问题转化为求和为sum(nums)-x的最长连续子数组的长度
        n = len(nums)
        res = n # operations times
        l, r = 0, 0
        count = 0
        target = sum(nums) - x
        if target == 0: return n
        if target < 0: return -1
        while r < n:
            count += nums[r]
            while count > target:
                count -= nums[l]
                l += 1
            if count == target:
                res = min(res, n - (r - l + 1))
            r += 1
        return res if res != n else -1