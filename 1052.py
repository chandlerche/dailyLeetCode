class Solution:
    def maxSatisfied(self, customers, grumpy, X):
        
        # 先找出 customers[0 到 X-1] 之间不满的顾客
        result = buffer = sum([customers[i] for i in range(len(customers[:X])) if grumpy[i]])
        
        # 滑动窗口，找出最多顾客不满的时段
        for i in range(X, len(customers)):
            buffer += customers[i]*grumpy[i] - customers[i-X]*grumpy[i-X]
            result = max(result, buffer)
        
        # 返回原本满意的顾客加上老板放大招后满意的顾客
        return sum([customers[i] for i in range(len(customers)) if grumpy[i] == 0])+result