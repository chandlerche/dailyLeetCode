class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD, lt, lw = 10 ** 9 + 7, len(target), len(words[0])
        F = lru_cache(None)( lambda c, t: sum(w[t] == c for w in words) )
        @lru_cache(None)
        def S(i, t):
            if i >= lt: return 1
            if t >= lw: return 0
            return (S(i, t + 1) + F(target[i], t) * S(i + 1, t + 1)) % MOD
        return S(0, 0)