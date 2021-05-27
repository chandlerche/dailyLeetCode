class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        nums = [0]+nums+[0]
        last_zero, result, negs = 0, 0, [] #上一个0的位置、结果、负数的位置

        for i in range(1,len(nums)): 
            if nums[i] == 0:
                if len(negs) % 2 ==0:   #偶数个负数，取整个子数组
                    result = max(result,i-last_zero-1)
                else:   #奇数个负数，要么剃掉第一个，要么剃掉最后一个
                    result = max(result,i-negs[0]-1,negs[-1]-last_zero-1) 
                last_zero = i
                negs = []
            elif nums[i] < 0:
                negs.append(i) #记录负数的位置

        return result