class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        
        zs = tuple([0 for i in range(n)])
        
        @lru_cache(None)
        def dp(n,state):
            if n == -1:
                if state == zs:
                    return 0
                else:
                    return -inf
            ans = dp(n-1,state)
            nstate = list(state)
            nstate[requests[n][0]] += 1
            nstate[requests[n][1]] -= 1
            ans = max(ans, dp(n-1,tuple(nstate)) + 1)
            return ans
        return dp(len(requests) - 1,zs)