class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        first = {}
        last = {}
        for i, ch in enumerate(s):
            last[ch] = i
            if ch not in first:
                first[ch] = i

        res = []
        stack = []

        def pop():
            _ = stack.pop()
            if len(stack) > 0:
                stack[-1][1] = max(stack[-1][1], _[1])  # update parent context
            return _

        for i, ch in enumerate(s):
            if i == first[ch]:
                stack.append([i, last[ch]])  # new context

            if i == last[ch] and len(stack) > 0 and i == stack[-1][1]:
                res.append(s[stack[-1][0]:i+1])
                _ = pop()
                while len(stack) > 0 and stack[-1][0] < _[0]:  # pop enclosing contexts
                    pop()

            while len(stack) > 0 and first[ch] < stack[-1][0]:  # pop corrupt contexts
                pop()

        return res