class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        sys.setrecursionlimit(1000000007)
        nums=[nums1,nums2]
        @lru_cache(None)
        def f(i,j,n):
            if i==len(nums[n]):
                return 0
            if j==len(nums[n^1]):
                return nums[n][i]+f(i+1,j,n)
            while nums[n][i]>nums[n^1][j]:
                j+=1
                if j==len(nums[n^1]):
                    return nums[n][i]+f(i+1,j,n)
            if nums[n][i]==nums[n^1][j]:
                return nums[n][i]+max(f(i+1,j,n),f(j+1,i,n^1))
            return nums[n][i]+f(i+1,j,n)
        return max(f(0,0,0),f(0,0,1))%1000000007