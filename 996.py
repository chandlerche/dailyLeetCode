class Solution:
    def numSquarefulPerms(self, A: List[int]) -> int:
        def ok(a: int, b: int) -> bool:
            c = int(sqrt(a + b))
            return c * c == a + b
        
        n, ans = len(A), 0
        
        def dfs(k: int = 0, pre: int = 0) -> None:
            nonlocal ans
            if k == n:
                ans += 1
                return 
            
            vis = set()
            for i in range(k, n):
                if A[i] not in vis and (ok(pre, A[i]) or k == 0):
                    vis.add(A[i])
                    A[k], A[i] = A[i], A[k]
                    dfs(k + 1, A[k])
                    A[k], A[i] = A[i], A[k]
        
        dfs()
        
        return ans