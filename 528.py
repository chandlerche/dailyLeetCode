import random
class Solution:
    def __init__(self, w: List[int]):
        self.len_w = len(w)
        self.presum = [0] * (self.len_w + 1)
        for i in range(self.len_w):
            self.presum[i + 1] = self.presum[i] + w[i]
        

    def pickIndex(self) -> int:
        num = random.random() * self.presum[-1]
        return self.binary_search(num) - 1

    def binary_search(self, num):
        left = 0
        right = self.len_w # presum比w长度多1

        while left < right:
            mid = (left + right) // 2

            if self.presum[mid] < num:
                left = mid + 1
            else:
                right = mid

        return right