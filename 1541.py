class Solution:
    def minInsertions(self, s: str) -> int:
        res = need_right = need_left = 0
        for c in s:
            if c == '(':
                if need_right % 2:
                    need_right -= 1
                    res += 1
                need_right += 2
            else:
                need_right -= 1
                if need_right < 0:
                    need_right += 2
                    need_left += 1
        return need_right + need_left + res