class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        def flip(n:str)->int:
            board = [line[:] for line in mat]
            for i in range(L):
                if n[i]=='1':
                    x,y = i % N, i // N
                    for dx,dy in [(x-1,y),(x,y),(x+1,y),(x,y-1),(x,y+1)]:
                        if 0<=dx<N and 0<=dy<M:
                            board[dy][dx] ^= 1
            return sum([sum(line) for line in board])

        M, N, L = len(mat), len(mat[0]), len(mat)*len(mat[0])
        template = '{:0'+str(L)+'b}'
        status = [template.format(n) for n in range(2**L)]
        status.sort(key=lambda x:x.count('1')) #这一句其实删掉也能过
        for n in status:
            if flip(n) == 0:
                return n.count('1')
        return -1