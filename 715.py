class RangeModule:

    def __init__(self):
        self.Range = list()

    def addRange(self, left: int, right: int) -> None:
        self.Range.append([left, right])
        self.Range.sort()
        i = 1
        while i < len(self.Range):
            al, ar, bl, br = self.Range[i - 1][0], self.Range[i - 1][1], self.Range[i][0], self.Range[i][1]
            # a区间包含b区间
            if ar >= br:
                del self.Range[i]
            # ab区间重叠
            elif ar >= bl:
                self.Range[i - 1][1] = br
                del self.Range[i]
            # ab区间不重叠
            else:   i += 1
        # print("added:", self.Range)

    def queryRange(self, left: int, right: int) -> bool:
        for intervals in self.Range:
            if intervals[0] <= left and right <= intervals[1]:    return True
        return False

    def removeRange(self, left: int, right: int) -> None:
        for i in range(len(self.Range)):
            al, ar = self.Range[i][0], self.Range[i][1]
            # 不重叠(left-right-al-ar)
            if right <= al:    break
            if left <= ar:
                # 包含(al-left-right-ar)
                if right <= ar:
                    self.Range[i][1] = left 
                    self.Range.append([right, ar])
                    self.Range.sort()
                    break
                # 重叠(al-left-ar-right)
                else:
                    self.Range[i][1] = left
                    left = ar
                    continue
        # print("removed:", self.Range)
        return

# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)