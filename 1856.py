class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        mod, n = 10 ** 9 + 7, len(nums)
        stack = []
        right_index = [0] * (n + 1) # 开区间
        left_index = [0] * (n + 1) # 闭区间
        pre_sum = [0]
        for i in nums:
            pre_sum.append(pre_sum[-1] + i)
        # 找每个数右边第一个比他小的位置
        for i, v in enumerate(nums + [-1]):
            while stack and v < stack[-1][1]:
                idx, val = stack.pop()
                right_index[idx] = i
            stack.append((i, v))
        # 找每个数左边第一个比他小的位置
        stack = []
        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[i] < stack[-1][1]:
                idx, val = stack.pop()
                left_index[idx] = i + 1
            stack.append((i, nums[i]))

        ans = 0
        for i in range(len(nums)):
            ans = max(ans, nums[i] * (pre_sum[right_index[i]] - pre_sum[left_index[i]]))
        return ans % mod