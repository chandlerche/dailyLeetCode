class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # 是3sum的followup题，简化版，解法类似，只是更简单了
        res = nums[0] + nums[1] + nums[len(nums) - 1] #先设置一个门槛，因为这题无论如何要有返回值的
        nums = sorted(nums)

        for i in range(len(nums) - 2):
            l , r = i + 1 , len(nums) - 1
            while l < r:
                sums = nums[i] + nums[l] + nums[r]
                if sums > target:
                    r -= 1
                else:
                    l += 1
                # 如果当前三数之和与目标值的距离比开始设置的基准值要更近，就更新基准值
                if abs(sums - target) < abs(res - target):
                    res = sums
        return res