class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        sum1, sum2 = sum(nums1), sum(nums2)
        if sum1 == sum2:
            return 0
        if sum1 > sum2:
            sum1, sum2 = sum2, sum1
            nums1, nums2 = nums2, nums1

        diff = sum2 - sum1
        cnt = [0] * 6
        for i in nums1:
            cnt[6 - i] += 1
        for i in nums2:
            cnt[i - 1] += 1

        ans = 0
        for i in range(5, 0, -1):
            t = cnt[i] * i
            if t >= diff:
                return ans + (diff - 1) // i + 1
            else:
                diff -= t
                ans += cnt[i]
        return -1