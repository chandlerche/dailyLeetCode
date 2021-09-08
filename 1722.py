class Solution:
    def minimumHammingDistance(self, source, target, allowedSwaps):
        """
        :type source: List[int]
        :type target: List[int]
        :type allowedSwaps: List[List[int]]
        :rtype: int
        """
        graph = collections.defaultdict(list)
        n = len(source)
        curr_hamming = 0
        for i, j in zip(source, target):
            if i != j:
                curr_hamming += 1
        if len(allowedSwaps) == 0:
            return curr_hamming

        for x, y in allowedSwaps:
            graph[x].append(y)
            graph[y].append(x)
        visited = [0] * n
        connect_index = []

        def dfs(curr, con):
            visited[curr] = 1
            con.add(curr)
            for v in graph[curr]:
                if visited[v] == 0:
                    dfs(v, connect)

        for i in range(n):
            if i not in graph:
                connect_index.append([i])
            elif not visited[i]:
                connect = set()
                dfs(i, connect)
                connect_index.append(list(connect))
        # print(connect_index)
        ans = 0
        for con in connect_index:
            curr_list_s = [source[i] for i in con]
            curr_list_t = [target[i] for i in con]
            t_counts = collections.Counter(curr_list_t)
            # print(t_counts)
            for s in curr_list_s:
                if s in t_counts and t_counts[s] > 0:
                    t_counts[s] -= 1
                else:
                    ans += 1
            # print(t_counts)
        return ans