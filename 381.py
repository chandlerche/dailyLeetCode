class RandomizedCollection:
    def __init__(self):
        self.vals=[]
        self.index={}
    def insert(self, val: int) -> bool:
        self.vals.append(val)
        if val in self.index:
            self.index[val].add(len(self.vals)-1)
            return False
        else:
            self.index[val] = {len(self.vals)-1}
            return True
    def remove(self,val):
        if val not in self.index:
            return False
        last = len(self.vals)-1
        idx = self.index[val].pop()
        if len(self.index[val])==0:
            del self.index[val]
        if idx!=last:
            self.vals[idx] = self.vals[last]
            self.index[self.vals[idx]].remove(last)
            self.index[self.vals[idx]].add(idx)
        self.vals.pop()
        return True
    def getRandom(self) -> int:
        if self.vals:
            return self.vals[random.randint(0,len(self.vals)-1)]