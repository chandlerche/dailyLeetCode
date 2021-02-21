class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = set()
        if len(board) < 1 or len(words) < 1:
            return []

        trie = Trie()
        for word in words:
            trie.insert(word)
        
        n = len(board)
        m = len(board[0])

        def backtrack(i, j, tmp, flags, node):
            if node.get("is_word", False):
                res.add(tmp[:])
            for x, y in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                ii = i + x
                jj = j + y
                if 0 <= ii < n and 0<=jj < m and flags[ii][jj] == 0 and board[ii][jj] in node.keys():
                    flags[ii][jj] = 1
                    backtrack(ii, jj, tmp + board[ii][jj], flags, node[board[ii][jj]])
                    flags[ii][jj] = 0
            return 
        
        for i in range(n):
            for j in range(m):
                if board[i][j] in trie.root.keys():
                    flags = [[0]*m for _ in range(n)]
                    flags[i][j] = 1
                    node = trie.root[board[i][j]]
                    backtrack(i, j, board[i][j], flags, node)
                    
        return list(res)

class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for s in word:
            if s in node.keys():
                node = node[s]
            else:
                node[s] = {}
                node = node[s]
        node["is_word"] = True