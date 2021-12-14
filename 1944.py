class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        ans = [0]*len(heights)
        stack = [] #单调递减栈，stack[-1]为栈顶元素（最小）
        for i in range(len(heights)-1, -1, -1):
            while stack and heights[i] > heights[stack[-1]]:
               ans[i] += 1
               stack.pop()
            #如果栈还存在，说明还能看到一个人
            if stack:
                ans[i] += 1
            stack.append(i)
        
        return ans