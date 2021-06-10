from sortedcontainers import SortedList
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        ls = SortedList([val<<1 if val&1 else val for val in nums])
        ans = ls[-1] - ls[0]
        while not ls[-1] & 1:
            ls.add(ls.pop()>>1)
            ans = min(ans, ls[-1] - ls[0])            
        return ans