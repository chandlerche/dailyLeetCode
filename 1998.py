from collections import defaultdict
from math import sqrt
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def get_root(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def union(self, x, y):
        rx, ry = self.get_root(x), self.get_root(y)
        self.parent[ry] = rx

    def is_union(self, x, y):
        return self.get_root(x) == self.get_root(y)

class Solution:
    def gcdSort(self, nums: List[int]) -> bool:
        primes = self.countPrimes(50000)
        n, m = len(nums), len(primes)
        primesIndex = {}
        for i in range(m):
            primesIndex[primes[i]] = n + i
        uf = UnionFind(n + m)
        posSet = defaultdict(list)
        for i in range(n):
            posSet[nums[i]].append(i)
            for j in range(1, int(sqrt(nums[i])) + 1):
                if nums[i] % j != 0:
                    continue
                if j in primesIndex:
                    uf.union(i, primesIndex[j])
                div = nums[i] // j
                if div in primesIndex:
                    uf.union(i, primesIndex[div])
        sortedNums = sorted(nums)
        for i in range(n):
            v = sortedNums[i]
            origin = posSet[v].pop()
            if not uf.is_union(i, origin):
                return False
        return True

    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        count = 0
        list = [True] * n
        prime = []
        for i in range(2,n,1):
            if list[i]:
                prime.append(i)
                count += 1
            j = 0
            while j < count and i * prime[j] < n:
                list[i * prime[j]] = False
                if i % prime[j] == 0:
                    break
                j += 1
        return prime