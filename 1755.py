class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        ans = abs(goal)
        n = len(nums)
        mi = n>>1
        cando = [set() for _ in range(2)]
        def dfs(i,cur,mynums,ccc):
            if i==len(mynums):
                cando[ccc].add(cur)
                return
            dfs(i+1,cur,mynums,ccc)
            dfs(i+1,cur+mynums[i],mynums,ccc)
        dfs(0,0,nums[:mi],0)
        dfs(0,0,nums[mi:],1)
        cando = [*map(list,cando)]
        cando[0].sort()
        cando[1].sort()
        le = 0
        ri = len(cando[1])-1
        l1 = len(cando[0])
        # print(cando)
        while le < l1 and ri >= 0:
            t = cando[0][le]+\
            cando[1][ri]
            ans = min(ans,abs(t-goal))
            if t>goal:
                ri -= 1
            elif t<goal:
                le += 1
            else:
                return 0
        return ans