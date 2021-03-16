class Solution:
    # 当num小于9，即只有一位时，直接返回num，大于9时，如果能被9整除，则返回9
    def addDigits(self, num: int) -> int:
        if num > 9:
            num = num % 9
            if num == 0:
                return 9
        return num