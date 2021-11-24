class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        counter = [[0]*101]
        for n in nums:
            cnt = counter[-1][:]
            cnt[n] += 1
            counter += [cnt]
        res = []
        for l, r in queries:
            right = counter[r + 1]
            left = counter[l]
            last = 0
            m = 101
            for i in range(101):
                if right[i] - left[i] > 0:
                    if last > 0:
                        m = min(m, i - last)
                    last = i
            if m == 101:
                m = -1
            res += [m] 
        return res