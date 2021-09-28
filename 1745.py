class Solution:
    def checkPartitioning(self, s: str) -> bool:
        if len(s)<3:return False
        def is_backword(word):
            return word==word[::-1]
        n = len(s)
        for i in range(1,n):
            if not is_backword(s[:i]):continue
            for j in range(i+1,n):
                if is_backword(s[i:j]) and is_backword(s[j:]):
                    return True
        return False