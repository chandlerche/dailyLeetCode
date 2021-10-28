class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        n = len(binary)
        mod = 10 ** 9 + 7
        zero = 0
        dp0,dp1 = 0,0
        for i in range(n - 1,-1,-1):
            if binary[i] == '0':
                zero = 1
                dp0 += (dp1 + 1) % mod
            else: 
                dp1 += (dp0 + 1) % mod
            
        return (dp1 + zero) % mod