class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if nums == None or len(nums) == 0: return [-1, -1]

        res = [-1,-1]
        map = {}
        for i in range(len(nums)):
            if map.__contains__(target - nums[i]):
                res[0] = map[target - nums[i]]
                res[1] = i
                break
            map[nums[i]] = i
        return res