class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def backtrack(track, choices):
            if len(track) == k:
                if sum(track) == n:
                    res.append(track)
                return
            
            for i in range(len(choices)):
                backtrack(track + [choices[i]], choices[i+1:])
        
        backtrack([], list(range(1, 10)))
        return res