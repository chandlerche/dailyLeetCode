class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 整体解题思路是把3sum化成2sum，遍历当前数的时候，看其后面的两个数有没有可能相加与该数抵消等于0
        res = []

        # 1. 为了方便下面去重，先把原数组排序
        nums = sorted(nums)

        # 2. 遍历数组里每个数（除了最后两个，因为至少留一个low和high两个指针）
        for i in range(len(nums) - 2):
            # i指针位置的去重，遍历的当前数如果重复，则右移，不需要重复计算
            if i > 0 and nums[i] == nums[i - 1]: continue
            # low指针从i后面第一位开始向右扫，high指针从最末一位向左扫
            low = i + 1
            high = len(nums) - 1
            sums = 0 - nums[i] # 其两数之和需要+sums = 0
            while low < high:
                if nums[low] + nums[high] == sums:
                    # 对符合条件的情况，加入最终结果的数组中
                    res.append([nums[i] , nums[low] , nums[high]])
                    # 检查low指针和high指针是否存在重复，如有就跳过
                    while low < high and nums[low] == nums[low + 1]: low += 1
                    while low < high and nums[high] == nums[high - 1]: high -= 1
                    low += 1
                    high -= 1
                # 如果两数之和小于i值，就使这个和变大一些，low指针右移，反之high指针左移
                elif nums[low] + nums[high] < sums:
                    low += 1
                else:
                    high -= 1
        return res