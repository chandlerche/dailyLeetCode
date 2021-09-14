class Solution:
    def maxLength(self, arr: List[str]) -> int:
        buf = [set(word) for word in arr if len(word)==len(set(word))]
        table = {'abcdefghijklmnopqrstuvwxyz'[i]:1<<i for i in range(26)}
        buf = [ (sum([table[c] for c in word]),len(word)) for word in buf]
        total = len(set(''.join(arr)))
        
        que = deque([(0,0)])
        footprint = {0}
        result = 0
        while que:
            mask,cnt = que.pop()
            if cnt > result:
                result = cnt
            for word,l in buf:
                if word&mask == 0 and not word|mask in footprint:
                    footprint.add(word|mask)
                    que.append((word|mask,cnt+l))
                    if cnt +l == total:
                        return total
        return result