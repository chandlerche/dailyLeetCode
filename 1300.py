class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        n = len(arr)
        arr.sort()
        pre = 0
        for i in range(n):
            curr_sum = pre + (n - i) * arr[i]
            if curr_sum >= target:
                value = (target - pre) // (n - i)
                sum_low = pre + value * (n - i)
                sum_high = sum_low + n - i
                return value if (target - sum_low) <= (sum_high - target) else value + 1
            pre += arr[i]

        return arr[-1]