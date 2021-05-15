class Solution(object):
    def minimumEffort(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: int
        """
        t_idx = list(range(len(tasks)))
        t_idx = sorted(t_idx, key=lambda k:tasks[k][1] - tasks[k][0])
        s = 0
        rest = []
        ans = 0
        for i in range(len(tasks)):
            ans = max (tasks[t_idx[i]][1] - tasks[t_idx[i]][0]  - s, ans)
            s += tasks[t_idx[i]][0] 
        
        return ans + s