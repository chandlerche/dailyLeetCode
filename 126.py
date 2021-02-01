class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[str]:
        d = collections.defaultdict(list)
        for word in wordList + [beginWord]:
            w = [*word]
            for i, c in enumerate(word):
                w[i] = '.'
                p = ''.join(w)
                d[p].append(word)
                d[word].append(p)
                w[i] = c
        if endWord in d:
            q, v = {beginWord: [[beginWord]]}, {beginWord}
            while q:
                if endWord in q:
                    return [*q[endWord]]
                t = collections.defaultdict(set)
                for i in q:
                    for j in d[i]:
                        for w in d[j]:
                            if w not in v:
                                t[w].update((*p, w) for p in q[i])
                q = t
                v.update(q.keys())
        return []