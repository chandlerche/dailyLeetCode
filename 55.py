class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        i = n-1
        while i >= 1:
            biaoji = 0
            for j in range(i-1,-1,-1):
                if j+nums[j] >= i:
                    i = j
                    biaoji = 1
                    break
            if biaoji == 0:
                return False
        return True