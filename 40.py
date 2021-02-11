class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def dfs(level, res_current):
            for i in range(level, len(candidates)):
                if i > level:
                    if candidates[i] == candidates[i - 1]: continue
                if sum(res_current) + candidates[i] == target:
                    res.append(res_current[:] + [candidates[i]])
                    return
                elif sum(res_current) + candidates[i] < target:
                    dfs(i + 1, res_current[:] + [candidates[i]])
                else: return
        dfs(0, [])
        return (res)