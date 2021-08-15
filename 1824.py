from collections import deque
class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        lens = len(obstacles)
        que = deque([[2, 0]])
        m = [[0] * lens for _ in range(3)]
        step = 0
        while que:
            n = len(que)
            step += 1
            for _ in range(n):
                cur = que.popleft()
                if cur[1] == lens - 1:
                    return step - lens
                for x, y in [(1, 0), (-1, 0), (0, 1)]:
                    nx, ny = cur[0] + x, cur[1] + y
                    if nx == 0:
                        nx = 3
                    if nx == 4:
                        nx = 1
                    if 1 <= nx <= 3 and 0 <= ny < lens and nx != obstacles[ny] and m[nx-1][ny] == 0:
                        que.append([nx, ny])
                        m[nx-1][ny] = 1