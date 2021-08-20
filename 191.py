class Solution:
    def hammingWeight(self, n: int) -> int:
        '''
        # Approach 1
        counter = 0
        while n != 0:
            n &= n - 1
            counter += 1
        return counter
        '''
        # Approach 2
        counter = 0
        for i in range(32):
            counter += n & 1
            n >>= 1
        return counter