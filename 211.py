class WordDictionary:

    def __init__(self):
        self.tree = {}

    def addWord(self, word: str) -> None:
        table = self.tree
        for c in word:
            if c not in table:
                table[c] = {}
            table = table[c]
        table["#"] = {}

    def dfs(self, word, cur, table):
        if cur == len(word):
            return "#" in table
        if word[cur] == ".":
            res = False
            for k, v in table.items():
                res = res or self.dfs(word, cur + 1, v)
            return res
        elif word[cur] in table:
            return self.dfs(word, cur + 1, table[word[cur]])
        else:
            return False

    def search(self, word: str) -> bool:
        return self.dfs(word, 0, self.tree)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)