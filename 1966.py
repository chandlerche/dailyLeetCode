class Solution:
    def binarySearchableNumbers(self, nums):
        n = len(nums)
        lft, rgh = [-1] * n, [n] * n
        
        stack = []
        for i in range(n):
            while stack and nums[i] > nums[stack[-1]]: stack.pop()
            if stack: lft[i] = stack[-1]
            stack.append(i)
            
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and nums[i] < nums[stack[-1]]: stack.pop()
            if stack: rgh[i] = stack[-1]
            stack.append(i)
            
        return sum(x == -1 and y == n for x, y in zip(lft, rgh))