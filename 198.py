class Solution:
    def rob(self, nums: List[int]) -> int:
        # curNo和curYes记录的是当前该数是否偷的利益结果
        curNo = 0
        curYes = 0
        for num in nums:
            temp = curNo
            curNo = max(curNo , curYes)
            curYes = temp + num
        return max(curYes , curNo)