class Solution(object):
    def smallestDivisor(self, nums, threshold):
        import math
        l = 1
        r = max(nums)
        mid = l + (r - l) // 2
        while l < r and mid > 0:
            mid = l + (r - l) // 2
            cur = 0
            for num in nums:
                    cur += math.ceil(float(num) / mid)
            if cur <= threshold:
                r = mid
            elif cur > threshold:
                l = mid + 1
        return l