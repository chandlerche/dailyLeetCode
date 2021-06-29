class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        hashset=[[] for _ in range(2*10**4+1)]
        self.hashset=hashset
        


    def add(self, key: int) -> None:
        
        if key not in self.hashset[key//50]:
            self.hashset[key//50].append(key)
        

    def remove(self, key: int) -> None:
        if key in self.hashset[key//50]:
            self.hashset[key//50].remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if key in self.hashset[key//50]:
            return True
        else:
            return False



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)