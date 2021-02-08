class Solution:
    def totalNQueens(self, n: int) -> int:

        def backtrack(x, col, dg1, dg2):
            if x == n:
                self.res += 1
                return
            
            for y in range(n):
                if y not in col and x + y not in dg1 and x - y not in dg2:
                    col.add(y)
                    dg1.add(x + y)
                    dg2.add(x - y)

                    backtrack(x + 1, col, dg1, dg2)

                    dg2.remove(x - y)
                    dg1.remove(x + y)
                    col.remove(y)        

        self.res = 0
        backtrack(0, set(), set(), set())
        return self.res