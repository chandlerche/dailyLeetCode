class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        self.memo = {}
        res = self.dfs(s1, s2, s3)
        return res
    
    @functools.lru_cache()
    def dfs(self, s1, s2, s3):
        l1, l2 = len(s1), len(s2)
        if l1 == 0 or l2 == 0:
            return s3 == s1 + s2
        key = ' '.join([s1, s2, s3])
        if key not in self.memo:
            flag = (s1[0] == s3[0] and self.isInterleave(s1[1:], s2, s3[1:]))
            flag |= (s2[0] == s3[0] and self.isInterleave(s1, s2[1:], s3[1:]))
            self.memo[key] = flag
        
        return self.memo[key]