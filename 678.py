class Solution:
    def checkValidString(self, s: str) -> bool:
        # 递归
        n = len(s)
        import functools
        @functools.lru_cache(None)
        def dfs(start, count):
            if count < 0: 
                return False
            for i in range(start, n):
                if s[i] == '(':
                    count += 1
                elif s[i] == ')':
                    if count == 0: 
                        return False
                    count -= 1
                elif s[i] == '*':
                    return dfs(i + 1, count + 1) or dfs(i + 1, count - 1) or dfs(i + 1, count) # # 作为左括号 or # 作为左括号 or 作为空
            return count == 0
        return dfs(0, 0)