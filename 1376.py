class Solution:
    def numOfMinutes(self, n, headID, manager, informTime):
        from collections import defaultdict
        children = defaultdict(list)
        for i,m in enumerate(manager):
            if m >= 0:
                children[m].append(i)
        def dfs(i):
            tmp = []
            for j in children[i]:
                tmp.append(dfs(j))
            return max(tmp or [0]) + informTime[i]
        return dfs(headID)