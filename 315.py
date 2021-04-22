class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        import bisect
        queue = []
        res = []
        for num in nums[::-1]:
            loc = bisect.bisect_left(queue, num)
            res.append(loc)
            queue.insert(loc, num)
        return res[::-1]