class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        big_cnt = [(1, (0, 0))]
        for row in range(len(forest)):
            for col in range(len(forest[0])):
                if forest[row][col] > 1:
                    big_cnt.append((forest[row][col], (row, col)))
        big_cnt.sort()
        res = 0
        strides = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        for i in range(len(big_cnt) - 1):
            stack = deque()
            stack.append((big_cnt[i][1], 0))
            vis = {big_cnt[i][1]}
            fail_flag = True
            while stack:
                ele = stack.popleft()
                if ele[0] == big_cnt[i + 1][1]:
                    res += ele[1]
                    fail_flag = False
                    break
                for s in strides:
                    new_s = (ele[0][0] + s[0], ele[0][1] + s[1])
                    if 0 <= new_s[0] < len(forest) and 0 <= new_s[1] < len(forest[0]):
                        if forest[new_s[0]][new_s[1]] != 0:
                            if new_s not in vis:
                                stack.append((new_s, ele[1] + 1))
                                vis.add(new_s)
            if fail_flag:
                return -1
        return res