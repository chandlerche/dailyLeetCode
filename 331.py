class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        degree = 1
        for node in preorder.split(','):
            if degree == 0:
                return False
            if node == '#':
                degree -= 1
            else:
                degree += 1
        return degree == 0