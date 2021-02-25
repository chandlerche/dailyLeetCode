class WordFilter:

    def __init__(self, words: List[str]):
        self.pre_d = {}
        self.words = words
        self.p_f_visit = {}
        self.p_visit = {}
        for i, word in enumerate(words):
            t = self.pre_d
            for c in word:
                if c not in t:
                    t[c] = {}
                t = t[c]
            t['val'] = i
        
    def f(self, prefix: str, suffix: str) -> int:
        if (prefix, suffix) in self.p_f_visit:
            return self.p_f_visit[(prefix, suffix)]
        if prefix not in self.p_visit:
            t = self.pre_d
            for c in prefix:
                if c not in t:
                    return -1
                t = t[c]
            pre_list = []
            def pre_dfs(d):
                if 'val' in d:
                    pre_list.append(d['val'])
                for t in d:
                    if t != 'val':
                        pre_dfs(d[t])
            pre_dfs(t)
            self.p_visit[prefix] = sorted(pre_list, reverse = True)
        for i in self.p_visit[prefix]:
            if self.words[i].endswith(suffix):
                self.p_f_visit[(prefix, suffix)] = i
                return i
        self.p_f_visit[(prefix, suffix)] = -1
        return -1



# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)