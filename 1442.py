class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        total_xor = [0]
        sum = 0
        for num in arr:
            total_xor.append(total_xor[-1]^num)
        for i in range(1, len(total_xor)):
            for k in range(i, len(total_xor)):
                if total_xor[i-1] == total_xor[k]:
                    sum += k - i
        return sum