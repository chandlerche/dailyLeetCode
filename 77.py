class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(arr,n,k):
            if k==1:
                return [[ele] for ele in arr]
            ans = [[arr[0]]+ele for ele in dfs(arr[1:],n-1,k-1)]
            if k<=n-1:
                ans += dfs(arr[1:],n-1,k)
            return  ans
        return dfs([i for i in range(1,n+1)],n,k)