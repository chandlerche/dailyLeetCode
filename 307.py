class FenwickTree:
    def __init__(self,n):
        self._sums = [0 for _ in range(n+1)]

    def update(self,i,delta):
        while i < len(self._sums):
            self._sums[i] += delta
            i += i & -i
    
    def query(self,i):
        s = 0
        while i > 0:
            s += self._sums[i]
            i -= i & -i
        return s

class NumArray:

    def __init__(self, nums: List[int]):
        self._nums = nums
        self._tree = FenwickTree(len(nums))
        for i in range(len(nums)):
            self._tree.update(i+1,nums[i])

    def update(self, i: int, val: int) -> None:
        self._tree.update(i+1,val-self._nums[i])
        self._nums[i] = val

    def sumRange(self, i: int, j: int) -> int:
        return self._tree.query(j+1)-self._tree.query(i)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)