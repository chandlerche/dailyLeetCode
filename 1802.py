class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:

        def get_sum(mid, count):
            ans = 0
            if mid >= count:
                ans = (mid + (mid - count + 1)) * count // 2
            else:
                ans = (mid + 1) * mid // 2 + (count - mid)
            return ans

        l = 1
        r = maxSum
        ans = 0
        while l <= r:
            mid = l + (r - l) // 2
            # 左边数的个数 index + 1 右边数的个数为 n - index
            left_sum = get_sum(mid, index + 1)
            right_sum = get_sum(mid, n - index)
            all_sum = left_sum + right_sum - mid
            if all_sum <= maxSum:
                l = mid + 1
                ans = mid
            else:
                r = mid - 1
        return ans