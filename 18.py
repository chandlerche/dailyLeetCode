class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        if len(nums) < 4:
            return res
        nums.sort()
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]: #如果和前一个数相等，就跳过
                continue
            for j in range(i + 1 , len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue #也是遇到一样就跳过 #从下面开始与3sum几乎一模一样
                low = j + 1
                high = len(nums) - 1
                while low < high:
                    sums = nums[i] + nums[j] + nums[low] + nums[high]
                    if sums == target:
                        res.append([nums[i] , nums[j] , nums[low] , nums[high]])
                        # 下面两步去重
                        while low < high and nums[low] == nums[low + 1]:
                            low += 1
                        while low < high and nums[high] == nums[high - 1]:
                            high -= 1
                        # 即便不需要去重，本身也要左移右移
                        low += 1
                        high -= 1
                    # 如果和小于目标值
                    elif sums < target:
                        low += 1
                    else:
                        high -= 1
        return res