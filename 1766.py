class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        @lru_cache()
        def dfs(node:int,num:int)->int:
            result = -1
            if gcd(nums[node],num)==1:
                return node
            if node == 0:
                return -1
            p = upper[node]
            result = dfs(p,num)
            return result

        graph = defaultdict(set)
        for a,b in edges:
            graph[a].add(b)
            graph[b].add(a)

        upper = [0]*len(nums)
        que = [0]
        while que:
            p = que.pop()
            for c in graph[p]:
                graph[c].discard(p)
                upper[c] = p
                que.append(c)

        result = [-1]*len(nums)
        for i in range(1,len(nums)):
            result[i] = dfs(upper[i],nums[i])
        return result