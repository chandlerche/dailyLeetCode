class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(nums[-1]+1):
            pos = len(nums) - bisect.bisect_left(nums,i)
            if pos == i:
                return pos
        return -1