class Solution:
    def sumSubarrayMins(self, A) -> int:
        if(len(A) == 0):
            return 0
        stack = []
        sum = 0
        A.insert(0,0)
        A.append(0)
        for i in range(len(A)):
            while stack and A[i]<A[stack[-1]]:
                out = stack.pop(-1)
                sum+=(out-stack[-1])*(i-out)*A[out]
            stack.append(i)
        return sum%(pow(10,9)+7)