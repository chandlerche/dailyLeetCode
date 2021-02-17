class Solution:
    def countArrangement(self, N: int) -> int:
     
        res = [False]*N
        result = []

        def dps(ltemp):
            if  ltemp[-1]%len(ltemp) != 0 and len(ltemp) % ltemp[-1] != 0:
                return 
            if len(ltemp) == N:
                result.append(ltemp[:])
            else:
                for i in range(N):
                    if res[i] == True:
                        continue
                    res[i] = True
                    dps(ltemp+[i+1])
                    res[i] = False
        dps([1])
        return len(result)