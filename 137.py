class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 异或运算^: 相同为0，不同为1
        # 与运算&  : 同时为1才为1
        # 取反运算符~: 按二进制数取反，0变1，1变0

        # 1.存入ones
        # 2.清空ones 存入twos
        # 3.清空twos
        # 实现效果就是出现3次的数字都会最终消失，出现1次的数字会留在ones中

        ones , twos = 0 , 0
        for num in nums:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones
        return ones