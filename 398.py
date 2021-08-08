class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        idx = -1
        n = 0
        for i in range(len(self.nums)):
            if self.nums[i] == target:
                n = n + 1
                if random.randint(1, n) == n:
                    idx = i
        return idx
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)