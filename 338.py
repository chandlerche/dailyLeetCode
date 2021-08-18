class Solution:
    def countBits(self, num: int) -> List[int]:
        outcome = [0]
        for i in range(1,num + 1):
            string = str(bin(i)).replace('0b','')
            outcome.append(string.count('1'))
        return outcome