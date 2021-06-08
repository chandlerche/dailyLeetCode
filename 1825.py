import bisect


class MKAverage:
    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.nums = []
        self.target_nums = []
        self.curr_sum = -1

    def addElement(self, num: int) -> None:
        out_num = 0
        if len(self.nums) == self.m:
            out_num = self.nums.pop(0)
        self.nums.append(num)
        if out_num:
            idx_out = bisect.bisect(self.target_nums, out_num) - 1
            if self.curr_sum != -1:
                if self.k <= idx_out < self.m - self.k:
                    self.curr_sum -= self.target_nums[idx_out]
                elif idx_out < self.k:
                    self.curr_sum -= self.target_nums[self.k]
                else:
                    self.curr_sum -= self.target_nums[self.m - self.k - 1]
            self.target_nums.pop(idx_out)

        idx_in = bisect.bisect(self.target_nums, num)
        bisect.insort(self.target_nums, num)
        if self.curr_sum != -1:
            if self.k <= idx_in < self.m - self.k:
                self.curr_sum += num
            elif idx_in < self.k:
                self.curr_sum += self.target_nums[self.k]
            else:
                self.curr_sum += self.target_nums[self.m - self.k - 1]

        if self.curr_sum == -1 and len(self.target_nums) == self.m:
            target = self.target_nums[self.k:self.m - self.k]
            self.curr_sum = sum(target)

    def calculateMKAverage(self) -> int:
        if len(self.target_nums) < self.m:
            return -1
        return self.curr_sum // (self.m - 2 * self.k)

# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()