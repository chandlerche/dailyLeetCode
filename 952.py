class Union:
    def __init__(self, size):
        self.elder = list(range(size))
        self.cnts = [0] * size

    def find(self, i):
        if i == self.elder[i]:
            return i
        else:
            ei = self.find(self.elder[i])
            self.elder[i] = ei
            return ei

    def union(self, i, j):
        ei, ej = self.find(i), self.find(j)
        if ei != ej:
            self.elder[ej] = ei
            self.cnts[ei] += self.cnts[ej]
class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        # 小于 100000^0.5 的最大质数为313
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313]
        large = {}
        u = Union(5200) # 50000以内质数一共5133个
        for n in nums:
            pre = None
            for i, p in enumerate(primes):
                if n == 1:
                    break
                if n % p == 0:
                    # 保证退出primes循环时，如果n>1，则n必为质数
                    while n % p == 0:
                        n //= p
                    if pre is None:
                        pre = i
                    else:
                        u.union(i, pre)
            if n > 50000:
                continue
            if n > 1:
                if n not in large:
                    large[n] = len(primes) + len(large)
                if pre is None:
                    pre = large[n]
                else:
                    u.union(large[n], pre)
            if pre is not None:
                u.cnts[u.find(pre)] += 1
        return max(max(u.cnts), 1)