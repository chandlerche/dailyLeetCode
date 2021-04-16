class SnapshotArray:
    '''我的思路就是用一个嵌套字典来记录更新，就好比我们拍快照的时候不会把整个系统全部都备份下来，而是会选择变化的部分记录下来，到时候恢复就直接根据拍下的快照和之前所有的快照结合起来就是我们要求的系统。'''

    def __init__(self, length: int):
        self.arr = [0 for _ in range(length)]
        self.count = 0					# 记录当前属于哪次snap
        self.dic = {self.count: {}}		# 记录更新的*嵌套字典*

    def set(self, index: int, val: int) -> None:
        self.dic[self.count][index] = val	# 更新嵌套字典
        self.arr[index] = val			# 同时也更新状态数组(即当前的状态)

    def snap(self) -> int:
        count = self.count
        self.count += 1
        self.dic[self.count] = {}		# 拍一次快照就是创建一个新的字典元素。
        return count

    def get(self, index: int, snap_id: int) -> int:
        val = self.dic.get(snap_id).get(index)	# 如果snap_id里面有那次更新则返回
        while not val:					# 如果没有更新，就迭代的寻找上一次的状态。
            if snap_id == 0:
                return 0
            snap_id -= 1
            val = self.dic.get(snap_id).get(index)
        return val


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)