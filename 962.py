class Solution:
    def maxWidthRamp(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        re = 0
        stack = []

        for i in range(len(A)):
            if len(stack) == 0 or A[stack[-1]] > A[i]:  # 防止下标越界，不用A[i]>A[i+1}
                stack.append(i)  # stack中存放下标 ，按值升序

        for j in range(len(A) - 1, re - 1, -1):  # 最大堆的左端肯定在单调栈内
            while stack and A[stack[-1]] <= A[j]:
                k = j - stack.pop()  # 对于栈顶元素来说不可能有更大值， 因此pop出
                re = max(re, k)  #找到每个单调递增堆中元素的最大宽度坡，max即为整个数组最终结果
        return re