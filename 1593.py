class Solution:
    def maxUniqueSplit(self, s: str) -> int:

        slices = set()
        self.res = 1

        def backtrack(subs):

            if not subs:
                self.res = max(self.res, len(slices))
                # print(slices)
                return

            for i in range(1, len(subs)+1):
                cur = subs[:i]              # 当前切下来的子串
                seen = cur in slices
                slices.add(cur)
                backtrack(subs[i:])
                if not seen:
                    slices.remove(cur)

        backtrack(s)
        return self.res