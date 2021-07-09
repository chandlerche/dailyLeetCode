class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 1  # i元素的左边累乘值
        right = 1  # i元素的右边累乘值
        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] *= left
            left *= nums[i]

            res[len(nums) - 1 - i] *= right
            right *= nums[len(nums) - 1 - i]
        return res