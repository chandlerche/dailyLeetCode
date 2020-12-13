class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        s = [set(), {''}]
        for c in expression:
            if c == ' ':
                continue
            elif c == '{':
                s.append(set())
                s.append({''})
            elif c == '}':
                s[-1] = {j + i for i in s.pop() | s.pop() for j in s[-1]}
            elif c == ',':
                s[-2], s[-1] = s[-2] | s[-1], {''}
            else:
                s[-1] = {i + c for i in s[-1]}
        return sorted(list(s[-2] | s[-1]))