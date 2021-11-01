class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        res = 0
        hash = {0}
        t = 0
        for n in nums:
            t += n
            if t - target in hash:
                res += 1
                hash = {0}
                t = 0
            else:
                hash.add(t)
        return res