class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        counter = [1] * len(parents)
        cnt = collections.Counter()
        children = defaultdict(list)
        for i, p in enumerate(parents):    
            children[p] += [i]
        def dfs(root=0):
            # print(root)
            for c in children[root]:
                counter[root] += dfs(c)
            return counter[root]
        dfs(0)
        # print(counter)
        res = 0
        for i, p in enumerate(parents):
            v = 1
            if p != -1:
                v *= counter[0] - counter[i]
            for c in children[i]:
                v *= counter[c]
            # print("remove", i, ", the score is:" , v)
            cnt[v] += 1
            res = max(res, v)
        # print(cnt)
        return cnt[res]