class BIT2D:
    def __init__(self, n1: int, n2: int):
        self.n1 = n1
        self.n2 = n2
        self._tree = [[0] * (n2 + 1) for _ in range(n1 + 1)]

    @staticmethod
    def _lowbit(x):
        return x & (-x)

    def update(self, i: int, j: int, x: int):
        now = self.query(i, j) - self.query(i - 1, j) - self.query(i, j - 1) + self.query(i - 1, j - 1)
        self.add(i, j, x - now)

    def add(self, i: int, j: int, x: int):
        i_lst, j_lst = [], []
        while i <= self.n1:
            i_lst.append(i)
            i += BIT2D._lowbit(i)
        while j <= self.n2:
            j_lst.append(j)
            j += BIT2D._lowbit(j)
        for ii in i_lst:
            for jj in j_lst:
                self._tree[ii][jj] += x

    def query(self, i: int, j: int) -> int:
        i_lst, j_lst = [], []
        while i > 0:
            i_lst.append(i)
            i -= BIT2D._lowbit(i)
        while j > 0:
            j_lst.append(j)
            j -= BIT2D._lowbit(j)
        ans = 0
        for ii in i_lst:
            for jj in j_lst:
                ans += self._tree[ii][jj]
        return ans

    def range_query(self, i1: int, j1: int, i2: int, j2: int) -> int:
        return self.query(i2, j2) - self.query(i2, j1 - 1) - self.query(i1 - 1, j2) + self.query(i1 - 1, j1 - 1)


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            n1, n2 = 0, 0
        else:
            n1, n2 = len(matrix), len(matrix[0])
        self.BIT2D = BIT2D(n1, n2)
        for i in range(n1):
            for j in range(n2):
                self.BIT2D.update(i + 1, j + 1, matrix[i][j])

    def update(self, row: int, col: int, val: int) -> None:
        self.BIT2D.update(row + 1, col + 1, val)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.BIT2D.range_query(row1 + 1, col1 + 1, row2 + 1, col2 + 1)