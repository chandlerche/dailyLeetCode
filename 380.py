import random

class RandomizedSet:
    def __init__(self):
        self.table = dict()
        self.stack = []

    def insert(self, val: int) -> bool:
        if val not in self.table:
            self.table[val] = len(self.stack)
            self.stack.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.table:
            self.stack[self.table[val]] = None
            self.table.pop(val)
            if len(self.table) * 2 < len(self.stack):
                self.stack = [v for v in self.stack if v is not None]
                self.table.update((v, i) for i, v in enumerate(self.stack))
            return True
        return False

    def getRandom(self) -> int:
        while True:
            i = random.randint(0, len(self.stack) - 1)
            if self.stack[i] is not None: return self.stack[i]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()