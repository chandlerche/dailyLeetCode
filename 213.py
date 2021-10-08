class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums , 0 , len(nums) - 2), self.helper(nums , 1 , len(nums) - 1))

    def helper(self , nums , l , r):
        curNo = 0
        curYes = 0
        for i in range(l , r + 1):
            temp = curNo # 保存上一轮没偷的话，一路加过来的总值
            curNo = max(curYes , curNo) # 当前不偷的话，那么上次一定偷了，就把上次yes的值更新过来
            curYes = temp + nums[i] #当前偷，说明上次没偷，上次没偷就把curNo保存的上回的值加上当前的num
        return max(curNo , curYes)

'''
[1 , 3 , 2 , 4 , 1]
      No   Yes
1:    0     1 
3:    1     3
'''