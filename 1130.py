class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        stack = []
        mct = 0
        for num in arr:
            while stack and num > stack[-1]:
                min_1 = stack.pop()
                if stack:
                    min_2 = min(stack[-1],num)
                else:
                    min_2 = num
                mct = mct + min_1 * min_2
            
            stack.append(num)
        
        while len(stack) > 1:
            mct = mct + stack.pop() * stack[-1]

        return mct; 