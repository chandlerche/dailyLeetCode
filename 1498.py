class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        mod = int(10**9+7)
        ret = 0
        l, r = 0, len(nums)-1
        while l<=r:
            if nums[l]+nums[r]>target:
                r -= 1
            else:
                ret = (ret + (1<<(r-l)))%mod
                l+=1
        return ret