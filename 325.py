from itertools import accumulate
class Solution:
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: list
        :type k: int
        :rtype: int
        """
        pre_sum = [0]+list(accumulate(nums))
        res = 0
        for i in range(len(pre_sum)):
            for j in range(i, len(pre_sum)):
                if pre_sum[j] - pre_sum[i] == k:
                    res = max(res, j - i)
        return res
