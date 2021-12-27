class Solution:
    def binarySearchableNumbers(self, nums):
        t1 = list(accumulate(nums, max))
        t2 = list(accumulate(nums[::-1], min))[::-1]
        return sum(x == y for x, y in zip(t1, t2))