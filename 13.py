class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        key = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }

        res = 0
        pre_value = 0
        for i in s:
            value = key[i]
            res += value
            if pre_value < value:
                res -= 2 * pre_value
            pre_value = value
        return res