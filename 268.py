class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 异或运算：相同为0，不同为1
        # 相同数字做异或运算都会等于0，最后留下的数字只能是丢失的数字
        res = len(nums)
        for i in range(len(nums)):
            # i的取值是[0,n-1]，而res等于n，此时去与nums里的值[0,n]做异或，只会留下多余的那个数
            res ^= i ^ nums[i]
        return res