class DetectSquares:
    def __init__(self):
        # 生成二维数组 grid[1005][1005]
        self.grid = [[0] * 1005 for _ in range(1005)]

    def add(self, point: List[int]) -> None:
        [x, y] = point
        # [x, y] 计数
        self.grid[x][y] += 1

    def count(self, point: List[int]) -> int:
        [x, y], res = point, 0
        # 对当前的 y 对应的那一条 x 轴进行枚举
        for x1 in range(0, 1001):
            # 获取这条 x 轴从左到右的有效点
            x_axis = self.grid[x1][y]
            if x_axis > 0 and x != x1:
                # 作差获得边长
                diff = abs(x - x1)
                # 检查这条 x 轴的上方有没有对应长度的 y_up、对角线 diag_up
                if y + diff <= 1000: 
                    y_up = self.grid[x][y + diff]
                    diag_up = self.grid[x1][y + diff]
                    if y_up > 0 and diag_up > 0:
                        # 排列组合，不同的点能组合多少个正方形
                        res += x_axis * y_up * diag_up
                # 检查这条 x 轴的下方有没有对应长度的 y_down、对角线 diag_down
                if 0 <= y - diff:
                    y_down = self.grid[x][y - diff]
                    diag_down = self.grid[x1][y - diff]
                    if y_down > 0 and diag_down > 0:
                        res += x_axis * y_down * diag_down
        return res

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)