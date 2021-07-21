class Solution(object):
    # 方向列表
    _DIRECTIONS = [(0, 1, "U"), (0, -1, "D"), (1, 0, "L"), (-1, 0, "R")]

    # 方向的反方向列表
    _OPPOSITE = {"U": "D", "D": "U", "L": "R", "R": "L"}

    def __init__(self):
        # 构造地图：从(500,500)出发，地图大小在[1,500]，所以需要1001来避免越界
        self.grid = [[0 for _ in range(1001)] for _ in range(1001)]

        self.visited = set()

        # 目标位置坐标
        self.target = (-1, -1)

        # 机器人变量
        self.master = None

    def findShortestPath(self, master: 'GridMaster') -> int:

        self.master = master

        # ---------- 深度优先搜索构造地图 ----------
        # 从(500,500)出发，地图大小在[1,500]，所以需要1001来避免越界
        self.grid[500][500] = True
        self.dfs(500, 500)

        # 在地图中没有找到目标位置
        if self.target == (-1, -1):
            return -1

        print("目标坐标:", self.target)

        # ---------- 广度优先搜索寻找最短路径 ----------
        # 构造维护当前最近距离的堆
        queue = collections.deque([(500, 500)])
        self.visited = {(500, 500)}

        ans = 0
        while queue:
            for _ in range(len(queue)):
                x1, y1 = queue.popleft()

                # 如果已经到达目标位置
                if (x1, y1) == self.target:
                    return ans

                for dx, dy, d in self._DIRECTIONS:
                    x2, y2 = x1 + dx, y1 + dy
                    if 0 <= x2 <= 1000 and 0 <= y2 <= 1000 and (x2, y2) not in self.visited and self.grid[x2][y2]:
                        self.visited.add((x2, y2))
                        queue.append((x2, y2))

            ans += 1

    def dfs(self, x, y):
        self.visited.add((x, y))

        # 判断当前位置是否为目标位置
        if self.master.isTarget():
            self.target = (x, y)

        for dx, dy, d in self._DIRECTIONS:
            if (x + dx, y + dy) not in self.visited and self.master.canMove(d):
                self.grid[x + dx][y + dy] = True
                self.master.move(d)  # 移动到当前位置
                self.dfs(x + dx, y + dy)
                self.master.move(self._OPPOSITE[d])
————————————————
版权声明：本文为CSDN博主「长行」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/Changxing_J/article/details/117223579