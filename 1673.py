class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        
        return self.removeKdigits(nums, len(nums) - k)
    def removeKdigits(self, num, k):
        stack = []
        remain = len(num) - k
        for digit in num:
            while k and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        return stack[:remain]