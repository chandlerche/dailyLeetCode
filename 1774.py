class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        res = []
        def dfs(index,cur):
            if (index == len(toppingCosts)):
                res.append(cur)
                return 
            dfs(index+1,cur)
            dfs(index+1,cur+toppingCosts[index])
            dfs(index+1,cur+2*toppingCosts[index])
        ans = float('inf')
        dfs(0,0)
        for i in range(len(baseCosts)):
            res.sort(key=lambda x : [abs(x-(target-baseCosts[i])),x])
        
            if (abs(res[0] + baseCosts[i] - target) < abs(ans-target)):      
                ans = res[0] + baseCosts[i]
            elif (abs(res[0] + baseCosts[i] - target) == abs(ans-target)):
                if ans > res[0] + baseCosts[i]:
                    ans = res[0] + baseCosts[i]
        return ans