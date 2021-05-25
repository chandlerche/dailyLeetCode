class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        odd = [0] * (len(A)+1)
        odd[0] = 1
        cnt, ans = 0, 0
        for num in A:
            cnt += num
            if cnt >= S:
                ans += odd[cnt-S]
            odd[cnt] += 1
        print(odd)
        return ans